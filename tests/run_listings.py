# -*- coding: utf-8 -*-
"""Chạy tuần tự các đoạn mã của giáo trình trên một phiên Spark cục bộ (đường dẫn cục bộ như trong notebook).

    python tests/run_listings.py            # tất cả chương
    python tests/run_listings.py 6 7        # chỉ chương 6 và 7
Kết quả: tests/report.md
"""
import io, json, os, platform, sys, time, traceback, contextlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, ROOT)
import pyspark
from pyspark.sql import SparkSession, functions as F

chapters = [int(a) for a in sys.argv[1:]] or list(range(1, 9))
items = json.load(open(os.path.join(ROOT, "tests", "listings.json"), encoding="utf-8"))["listings"]

def new_session():
    return (SparkSession.builder.master("local[2]").appName("giao-trinh-du-lieu-lon")
            .config("spark.ui.enabled", "false").config("spark.driver.host", "127.0.0.1")
            .config("spark.sql.shuffle.partitions", "8").getOrCreate())

import shutil
for thu_muc in ("output", "models"):
    shutil.rmtree(os.path.join(ROOT, thu_muc), ignore_errors=True)
rows = []
for ch in chapters:
    spark = new_session(); sc = spark.sparkContext; sc.setLogLevel("ERROR")
    ns = {"spark": spark, "sc": sc, "F": F}
    for it in [i for i in items if i["ch"] == ch]:
        tag = f"Đoạn mã {it['ch']}.{it['num']}"
        if it["skip"]:
            rows.append((tag, it["title"], "BỎ QUA", it["skip"], 0.0)); continue
        t0 = time.time(); buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                if it["prep"]:
                    exec(compile(it["prep"], f"{tag}-prep", "exec"), ns)
                code = "\n".join(l for l in it["code"].split("\n") if not l.lstrip().startswith("!"))
                exec(compile(code, tag, "exec"), ns)
            status, note = "ĐẠT", buf.getvalue().strip().split("\n")[-1][:80] if buf.getvalue().strip() else ""
        except Exception as e:
            status, note = "LỖI", f"{type(e).__name__}: {str(e).splitlines()[0][:160]}"
        rows.append((tag, it["title"], status, note, time.time() - t0))
        # neu doan ma da dung phien Spark thi tao lai
        if ns["spark"]._jsc is None or ns["spark"].sparkContext._jsc is None:
            spark = new_session(); ns["spark"], ns["sc"] = spark, spark.sparkContext
    spark.stop()

ok = sum(r[2] == "ĐẠT" for r in rows); bad = sum(r[2] == "LỖI" for r in rows); skip = sum(r[2] == "BỎ QUA" for r in rows)
lines = [f"# Kết quả chạy các đoạn mã trên môi trường tham chiếu ({ok} chạy được, {bad} lỗi, {skip} bỏ qua)\n",
         f"Môi trường: PySpark {pyspark.__version__}, Python {platform.python_version()}, Spark local[2]; chạy bằng `python tests/run_listings.py`.\n",
         "| Đoạn mã | Tên | Kết quả | Ghi chú | Thời gian (s) |", "|---|---|---|---|---|"]
for tag, title, st, note, dt in rows:
    lines.append(f"| {tag} | {title} | {st} | {note.replace('|', '/')} | {dt:.1f} |")
open(os.path.join(ROOT, "tests", "report.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines))
sys.exit(1 if bad else 0)
