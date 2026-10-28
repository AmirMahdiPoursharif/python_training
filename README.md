# تمرین‌های پایتون (python_training)

مجموعه‌ای از تمرین‌های مقدماتی پایتون برای تمرین مفاهیم پایه: توابع، شرط‌ها، حلقه‌ها، کار با رشته و لیست، دریافت ورودی از کاربر، کار با فایل و نوشتن تست.

هر تمرین از چهار بخش تشکیل شده است:

| بخش | توضیح |
| --- | --- |
| `readme.md` | صورت تمرین، توابع موردنیاز، مثال ورودی/خروجی و مفاهیم استفاده‌شده |
| پوشه‌ی کد تمرین | اسکلت برنامه که باید تکمیل شود (توابع خالی یا `pass`) |
| `tests/` | تست‌های `pytest` که رفتار مورد انتظار را مشخص می‌کنند |
| `solution/` | پاسخ مرجع برای مقایسه بعد از حل تمرین |

> این مخزن یک پروژه‌ی تمرینی است و بسته‌ی قابل نصبی (package) ندارد؛ همه‌ی دستورها با `uv run` و از ریشه‌ی پروژه (پوشه‌ای که `pyproject.toml` در آن است) اجرا می‌شوند.

---

## فهرست

- [ساختار پروژه](#ساختار-پروژه)
- [پیش‌نیازها](#پیشنیازها)
- [۱. دریافت پروژه (Clone)](#۱-دریافت-پروژه-clone)
- [۲. نصب وابستگی‌ها](#۲-نصب-وابستگیها)
- [۳. اجرای برنامه‌ها](#۳-اجرای-برنامهها)
- [۴. اجرای تست‌ها](#۴-اجرای-تستها)
- [۵. اجرای Ruff (لینت و فرمت)](#۵-اجرای-ruff-لینت-و-فرمت)
- [۶. اندازه‌گیری پوشش تست (Coverage)](#۶-اندازهگیری-پوشش-تست-coverage)
- [جدول تمرین‌ها](#جدول-تمرینها)
- [وضعیت فعلی مخزن](#وضعیت-فعلی-مخزن)
- [عیب‌یابی](#عیبیابی)
- [روند پیشنهادی برای حل هر تمرین](#روند-پیشنهادی-برای-حل-هر-تمرین)

---

## ساختار پروژه

```text
python_training/
├── pyproject.toml          # تنظیمات پروژه، وابستگی‌ها، pytest و ruff
├── uv.lock                 # قفل نسخه‌ی دقیق وابستگی‌ها
├── .python-version         # نسخه‌ی پایتون محیط توسعه (3.10)
├── README.md
└── src/
    ├── 001_temperature_conversion/
    │   ├── readme.md                   # صورت تمرین
    │   ├── temperature_conversion/     # اسکلت کد تمرین
    │   │   ├── main.py
    │   │   ├── convertor.py
    │   │   └── tests/
    │   └── solution/                   # پاسخ مرجع
    ├── 002_average_grades/
    ├── ...
    └── 008_text_file_analysis/
```

نکته‌ها:

- پوشه‌های تمرین با یک شماره‌ی سه‌رقمی شروع می‌شوند.
- پوشه‌ی داخلی هر تمرین، پکیج پایتون همان تمرین است (مثلاً `temperature_conversion`).

---

## پیش‌نیازها

| ابزار | نسخه‌ی موردنیاز | کاربرد |
| --- | --- | --- |
| Python | `>= 3.10` | اجرای کدها |
| uv | نسخه‌ی جدید (مثلاً `0.12`) | مدیریت محیط مجازی، نصب وابستگی‌ها و اجرای دستورها |
| Git | هر نسخه‌ی جدید | دریافت کد از GitHub |

بررسی نصب بودن ابزارها:

```bash
python --version
uv --version
git --version
```

## ۱. دریافت پروژه (Clone)

پروژه را از GitHub دریافت کنید:

```bash
git clone https://github.com/AmirMahdiPoursharif/python_training.git
cd python_training
```

### شاخه‌ها

- `main`
- `dev` 

برای دیدن شاخه‌ها:

```bash
git branch -a
```

---

## ۲. نصب وابستگی‌ها

در ریشه‌ی پروژه اجرا کنید:

```bash
uv sync
```

این دستور:

1. محیط مجازی `.venv` را می‌سازد (اگر وجود نداشته باشد).
2. نسخه‌ی پایتون مناسب را (بر اساس `.python-version`) آماده می‌کند.
3. وابستگی‌های پروژه و گروه `dev` را نصب می‌کند: `pytest`، `ruff` و `coverage`.
4. نسخه‌ها را طبق `uv.lock` ثابت نگه می‌دارد.

گزینه‌های پرکاربرد:

```bash
uv sync --no-dev      # فقط وابستگی‌های اصلی، بدون ابزارهای توسعه
uv sync --upgrade     # به‌روزرسانی وابستگی‌ها در محدوده‌ی مجاز
```

### نسخه‌ی پایتون و سازگاری با ۳.۱۰+

- حداقل نسخه‌ی پشتیبانی‌شده **Python 3.10** است (`requires-python = ">=3.10"` در `pyproject.toml`).
- `.python-version` روی `3.10` تنظیم شده تا محیط توسعه دقیقاً با کف نسخه‌های پشتیبانی‌شده ساخته شود و ناسازگاری‌ها زودتر دیده شوند.
- `ruff` هم با `target-version = "py310"` تنظیم شده تا سینتکس‌های مخصوص نسخه‌های جدیدتر (۳.۱۱+) را پیشنهاد یا تحمیل نکند.
- کدها فقط از قابلیت‌های موجود در ۳.۱۰ استفاده می‌کنند (`match`، `X | Y` در تایپ‌هینت‌ها) و ابزارها و تست‌ها با نسخه‌ی ۳.۱۰ اجرا شده‌اند.

اجرا با نسخه‌ی دیگری از پایتون (محیط `.venv` با همان نسخه بازسازی می‌شود):

```bash
uv sync --python 3.12             # ساخت/بازسازی محیط با ۳.۱۲
uv run pytest                     # اجرا داخل همان محیط
uv sync                           # بازگشت به نسخه‌ی .python-version (۳.۱۰)
uv python pin 3.12                # تغییر دائمی نسخه‌ی پروژه
uv python install 3.10 3.12 3.13  # نصب چند نسخه به‌صورت هم‌زمان
```

> اگر روی سیستم شما چند نسخه‌ی پایتون نصب است، `uv` نسخه‌ی خواسته‌شده در `.python-version` را انتخاب می‌کند؛ در صورت نبودن، همان را دانلود می‌کند.

### فعال‌کردن محیط مجازی (اختیاری)

معمولاً نیازی به فعال‌سازی نیست، چون `uv run` خودش دستور را داخل محیط پروژه اجرا می‌کند. اما اگر می‌خواهید `python` و `pytest` را مستقیم صدا بزنید:

ویندوز (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

مک و لینوکس:

```bash
source .venv/bin/activate
```

خروج از محیط:

```bash
deactivate
```

---

## ۳. اجرای برنامه‌ها

هر تمرین یک فایل `main.py` دارد که نقطه‌ی شروع برنامه است. از پوشه تمرین :

```bash
cd .\src\007_caesar_cipher\ 
uv run python -m caesar_cipher.main
```


نمونه برای چند تمرین:

```bash
uv run python -m temperature_conversion.main
uv run python -m palindrome.main
uv run python -m text_file_analysis.main
```

با اجرای این دستور، برنامه‌ی همان تمرین اجرا می‌شود و اگر پیاده‌سازی نشده باشد، فقط کار خاصی انجام نمی‌دهد (`main` خالی است).

### اجرای پاسخ‌های مرجع (`solution`)

پاسخ مرجع هر تمرین در پوشه‌ی `solution` قرار دارد. برای اجرای آن، به پوشه‌ی `solution` بروید و فایل را اجرا کنید:

```bash
cd src/004_multiplication_table/solution
uv run python main.py
```

چند پاسخ مرجع (مثل تمرین‌های ۱ و ۶) از `import` نسبی استفاده می‌کنند و با اجرای مستقیم فایل خطای `attempted relative import with no known parent package` می‌دهند. در این حالت، از پوشه‌ی خود تمرین آن را به‌صورت ماژول اجرا کنید:

```bash
cd src/001_temperature_conversion
uv run python -m solution.main
```

---

## ۴. اجرای تست‌ها

ابزار تست این پروژه `pytest` است و در `pyproject.toml` تنظیم شده است:

- `testpaths = ["src"]`: جست‌وجوی تست‌ها فقط داخل `src` انجام می‌شود.
- `python_files = ["test_*.py"]`: فقط فایل‌هایی که نامشان با `test_` شروع می‌شود.
- `python_functions = ["test_*"]`: فقط توابعی که نامشان با `test_` شروع می‌شود.
- `addopts = "-ra"`: خلاصه‌ی تست‌های رد‌شده و دلایل آن‌ها در پایان چاپ می‌شود.

اجرای تمام تست‌ها از ریشه‌ی پروژه:

```bash
uv run pytest
```

حالت پرجزئیات:

```bash
uv run pytest -v
```

اجرای تست‌های یک تمرین:

```bash
uv run pytest src/001_temperature_conversion -v
```

اجرای یک فایل تست مشخص:

```bash
uv run pytest src/001_temperature_conversion/temperature_conversion/tests/test_convertor.py -v
```

اجرای تست‌هایی که نامشان شامل یک عبارت است:

```bash
uv run pytest -k palindrome -v
```

اجرای فقط تست‌هایی که در اجرای قبلی شکست خورده‌اند:

```bash
uv run pytest --lf
```

توقف در اولین شکست:

```bash
uv run pytest -x
```

### تست‌های چالشی

بعضی تمرین‌ها فایل تست اضافه‌ای برای «چالش‌ها» دارند که نام آن با `test_` شروع نمی‌شود (مثل `average_grades_challenges.py`)، بنابراین با `uv run pytest` به‌صورت خودکار کشف نمی‌شوند. برای اجرای آن‌ها مسیر فایل را مستقیم بدهید:

```bash
uv run pytest src/002_average_grades/average_grades/tests/average_grades_challenges.py -v
```

### خواندن خروجی تست‌ها

| نشانه | معنی |
| --- | --- |
| `PASSED` | تست با موفقیت اجرا شد |
| `FAILED` | تست اجرا شد اما نتیجه با انتظار مطابقت ندارد |
| `ERROR` | هنگام جمع‌آوری یا آماده‌سازی تست خطایی رخ داد (مثلاً `ImportError` به‌خاطر تابع پیاده‌سازی‌نشده) |
| `collected 0 items` | تستی برای اجرا پیدا نشد (مسیر یا الگوی نام‌گذاری را بررسی کنید) |

---

## ۵. اجرای Ruff (لینت و فرمت)

`ruff` هم برای بررسی کیفیت کد (lint) و هم برای قالب‌بندی (format) استفاده می‌شود و در `pyproject.toml` تنظیم شده است:

- `line-length = 88`
- `target-version = "py310"`
- قواعد فعال: `E` (خطاهای سبک PEP 8)، `F` (خطاهای منطقی)، `I` (مرتب‌سازی importها)، `UP` (مدرن‌سازی کد)، `B` (قواعد باگ‌یاب)
- فرمت: کوتیشن دوتایی و تورفتگی با فاصله

بررسی کد بدون تغییر فایل‌ها:

```bash
uv run ruff check .
```

بررسی و اصلاح خودکار خطاهای قابل‌رفع:

```bash
uv run ruff check --fix .
```

دیدن تفاوت‌هایی که `--fix` اعمال می‌کند، بدون تغییر فایل‌ها:

```bash
uv run ruff check --diff .
```

قالب‌بندی همه‌ی فایل‌ها:

```bash
uv run ruff format .
```

بررسی قالب‌بندی بدون تغییر فایل‌ها (مناسب برای CI):

```bash
uv run ruff format --check .
```

اجرای `ruff` فقط روی یک تمرین:

```bash
uv run ruff check src/001_temperature_conversion
uv run ruff format src/001_temperature_conversion
```

روش پیشنهادی قبل از هر commit:

```bash
uv run ruff check --fix .
uv run ruff format .
uv run pytest
```

> اگر `ruff check` روی فایل‌های `solution` خطا داد، قبل از تغییر آن‌ها مطمئن شوید پاسخ مرجع را عمداً تغییر می‌دهید؛ هدف این پوشه، ارائه‌ی یک راه‌حل درست و خوانا است.

---

## ۶. اندازه‌گیری پوشش تست (Coverage)

بسته‌ی `coverage` در گروه `dev` نصب می‌شود. برای اندازه‌گیری پوشش:

```bash
uv run coverage run -m pytest src/002_average_grades
uv run coverage report -m
```

گزارش HTML:

```bash
uv run coverage html
```

سپس فایل `htmlcov/index.html` را در مرورگر باز کنید.

> گزارش `coverage` را روی تمرینی اجرا کنید که تست‌هایش کامل‌اند؛ در غیر این صورت عدد پوشش گمراه‌کننده است.

---

## وضعیت فعلی مخزن

این مخزن به‌صورت «تمرین» نگه‌داری می‌شود؛ یعنی:

- پکیج‌های تمرین عمداً اسکلت هستند (`main.py` با `pass` یا فایل‌های خالی). تا وقتی توابع پیاده‌سازی نشوند، `uv run pytest` خطا و شکست نشان می‌دهد. این رفتار مورد انتظار است و نشانه‌ی خرابی پروژه نیست.
- پوشه‌های `solution/` پاسخ مرجع و کامل همان تمرین‌ها هستند.
- ممکن است `uv run ruff check .` هم چند خطا و فایل قالب‌بندی‌نشده گزارش کند. برای رفع آن‌ها از `ruff check --fix` و `ruff format` استفاده کنید.

معیار پذیرش یک تمرین:

1. `uv run pytest src/<تمرین> -v` بدون `FAILED` و `ERROR` تمام شود.
2. `uv run ruff check src/<تمرین>` بدون خطا باشد.
3. `uv run ruff format --check src/<تمرین>` تغییری پیشنهاد نکند.

---

## عیب‌یابی

| مشکل | علت و راه‌حل |
| --- | --- |
| `uv: command not found` یا `uv is not recognized` | `uv` نصب نیست یا در `PATH` نیست. ترمینال را ببندید و دوباره باز کنید؛ در صورت نیاز دوباره نصب کنید. |
| `ModuleNotFoundError: No module named 'pytest'` | وابستگی‌ها نصب نشده‌اند. `uv sync` را در ریشه‌ی پروژه اجرا کنید. |
| `ImportError: cannot import name ...` هنگام اجرای تست‌ها | تابع مورد انتظار تست هنوز در پکیج تمرین پیاده‌سازی نشده است. فایل‌های پکیج را کامل کنید. |
| `no tests ran` | مسیر یا نام فایل تست اشتباه است؛ فایل‌های تست باید با `test_` شروع شوند و داخل `src` باشند. |
| `UnicodeEncodeError` یا به‌هم‌ریختگی متن فارسی در ویندوز | کدگذاری کنسول را UTF-8 کنید: `chcp 65001` و `$env:PYTHONIOENCODING="utf-8"`. |
| `No interpreter found for Python 3.10` | نسخه‌ی ۳.۱۰ نصب نیست؛ `uv python install 3.10` را اجرا کنید (یا `uv sync` بگذارید خودش دانلود کند). |
| خطای `requires-python` هنگام `uv sync` | نسخه‌ی پایتون فعال قدیمی‌تر از ۳.۱۰ است. `uv python pin 3.10` و سپس `uv sync` را اجرا کنید. |
| `cd` به مسیر پروژه خطا می‌دهد | مسیرهای دارای فاصله را داخل دابل‌کوتیشن بگذارید. |
| تغییرات `ruff` را نمی‌خواهم | به‌جای `ruff format .` از `ruff format --check .` استفاده کنید تا فقط بررسی شود. |

---

## روند پیشنهادی برای حل هر تمرین

1. صورت تمرین را بخوانید: `src/<تمرین>/readme.md`.
2. کد تمرین را پیاده‌سازی کنید (نه `solution`).
3. تست‌های همان تمرین را اجرا کنید:

   ```bash
   uv run pytest src/<تمرین> -v
   ```

5. کد را با `ruff` تمیز کنید:

   ```bash
   uv run ruff check --fix src/<تمرین>
   uv run ruff format src/<تمرین>
   ```

6. در پایان، پاسخ خود را با `solution/` مقایسه کنید. تفاوت راه‌حل‌ها اشکالی ندارد؛ مهم درست‌بودن رفتار و خوانایی کد است.

مفاهیمی که در این تمرین‌ها مرور می‌شوند:

- تعریف تابع، پارامتر و `return`
- شرط `if`/`elif`/`else` و `match`
- حلقه‌های `while` و `for`
- کار با `str`، `list` و `dict`
- دریافت ورودی با `input()` و تبدیل نوع
- مدیریت خطا با `try`/`except` (`ValueError`، `ZeroDivisionError`)
- کار با فایل و مسیرها
- تست‌نویسی با `pytest`، `parametrize` و `monkeypatch`

---

## مشارکت

- شاخه‌ی اصلی توسعه `dev` است؛ تغییرات را روی یک شاخه‌ی جدا بسازید و درخواست ادغام بدهید.

  ```bash
  git switch -c feature/my-exercise
  ```

- قبل از ارسال تغییرات، این سه دستور را اجرا کنید:

  ```bash
  uv run ruff check --fix .
  uv run ruff format .
  uv run pytest
  ```

- برای تمرین جدید، یک پوشه با الگوی `src/00X_name/` بسازید که شامل `readme.md`، پکیج تمرین، `tests/` و `solution/` باشد.

---

## نویسنده

- **AmirMahdiPoursharif** — [poursharif1386@gmail.com](mailto:poursharif1386@gmail.com)
- مخزن: [github.com/AmirMahdiPoursharif/python_training](https://github.com/AmirMahdiPoursharif/python_training)
