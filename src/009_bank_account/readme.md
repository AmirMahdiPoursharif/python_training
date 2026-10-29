# حساب بانکی (Bank Account)

## هدف تمرین

در این تمرین، یک برنامه‌ی حساب بانکی می‌سازیم که موجودی حساب را نگه می‌دارد و عملیات رایج بانکی را انجام می‌دهد:

- مشاهده‌ی موجودی
- واریز
- برداشت
- تغییر رمز عبور
- نمایش مشخصات حساب

نکته‌ی اصلی این تمرین، **رمزنگاری رمز عبور** است. رمز عبور به‌صورت متن ساده ذخیره نمی‌شود؛ هر حساب یک کلید تصادفی بین `1` تا `9` می‌گیرد و رمز عبور با **رمز سزار** (همان روش تمرین ۷) رمزگذاری می‌شود. برای بررسی رمز واردشده، آن را با همان کلید رمزگشایی و با رمز اصلی مقایسه می‌کنیم.

برنامه تعاملی است و منوها با کتابخانه‌ی `questionary` نمایش داده می‌شوند.

قوانین این تمرین:

- هر حساب فقط با رمز عبور درست به موجودی و عملیات خودش دسترسی دارد.
- رمز عبور با کلید تصادفی `1` تا `9` رمزگذاری می‌شود.
- پیام خطای رمز اشتباه در همه‌ی عملیات‌ها یکسان است: `password is not correct try again`
- موجودی و مبلغ واریز/برداشت می‌توانند صحیح یا اعشاری باشند.
- واریز یا برداشت با رمز اشتباه، هیچ تغییری در موجودی ایجاد نمی‌کند.
- برداشت بیشتر از موجودی انجام نمی‌شود و موجودی تغییر نمی‌کند.

## نحوه عملکرد برنامه

1. برنامه با پیام `Welcome to Bank Account` شروع می‌شود.
2. منوی اول دو گزینه دارد: ساخت حساب یا خروج. با انتخاب خروج، تابع `main()` رشته‌ی `So long` را برمی‌گرداند.
3. تابع `create_account()` با یک فرم سه‌فیلدی نام، موجودی و رمز عبور را می‌گیرد. هر فیلد تابع اعتبارسنجی مخصوص خودش را دارد.
4. موجودی با `float()` به عدد اعشاری تبدیل می‌شود و یک شیء `BankAccount` ساخته می‌شود.
5. در سازنده‌ی حساب، یک کلید تصادفی تولید و رمز عبور رمزگذاری می‌شود.
6. منوی دوم شش گزینه دارد و تا زمانی که کاربر خروج را انتخاب نکند تکرار می‌شود.
7. برای هر عملیات، رمز عبور گرفته می‌شود، رمزگشایی می‌شود و با رمز اصلی مقایسه می‌شود.
8. نتیجه‌ی هر عملیات با `print()` چاپ می‌شود. تابع `main()` فقط هنگام خروج یک رشته برمی‌گرداند:
   - `So long` در خروج از منوی اول
   - `have a nice day` در خروج از منوی عملیات

### نمونه اجرا

از پوشه‌ی تمرین:

```bash
uv run python -m bank_account.main
```

یک نمونه تعامل با برنامه:

```text
Welcome to Bank Account
? How can we help you?  Create Account
? whats your name?  Sara
? whats your balance?  1500
? whats your password?  ********
? What do you want to do?  Deposit to your account
? please enter your account password  ********
? please enter your amount  250
Done
your balance is: 1750.0
? What do you want to do?  Exit
have a nice day
```

> چون موجودی در `create_account()` با `float()` تبدیل می‌شود، در پیام‌ها به‌صورت `1500.0` و `1750.0` نمایش داده می‌شود. اگر حساب را مستقیم با عدد صحیح بسازید (مثل `BankAccount(1000, "Sara", "secret1")`)، پیام‌ها عدد صحیح نشان می‌دهند.

گزینه‌های منوی عملیات:

| گزینه | عملکرد | متد فراخوانی‌شده |
| --- | --- | --- |
| `1` | نمایش موجودی | `get_balance()` |
| `2` | واریز | `deposit()` |
| `3` | برداشت | `withdraw()` |
| `4` | تغییر رمز عبور | `change_password()` |
| `5` | نمایش مشخصات حساب | `account_detail()` |
| `0` | خروج | برگشت رشته‌ی `have a nice day` |

در صورت انتخاب گزینه‌ای خارج از این موارد، پیام `please select an option` چاپ می‌شود و منو دوباره نمایش داده می‌شود.

## ساختار برنامه

| فایل | نقش |
| --- | --- |
| `bank_account/account.py` | کلاس `BankAccount` و منطق عملیات حساب |
| `bank_account/cryptographer.py` | رمز سزار و توابع `encrypt()` و `decrypt()` |
| `bank_account/validator.py` | اعتبارسنجی نام، موجودی و رمز عبور |
| `bank_account/services.py` | ساخت حساب از روی فرم ورودی کاربر |
| `bank_account/main.py` | منوها و روند اجرای برنامه |

## توابع و کلاس‌های مورد نیاز

### کلاس `BankAccount`

**محل تعریف:** `bank_account/account.py`

این کلاس وضعیت یک حساب را نگه می‌دارد و همه‌ی عملیات بانکی را انجام می‌دهد.

در نمونه‌های زیر موجودی اولیه `1000` و رمز عبور `secret1` در نظر گرفته شده و هر نمونه از همین حالت شروع می‌شود.

#### `__init__(self, balance: float | int, name: str, password: str)`

الزامات:

- موجودی و نام را در صفت‌های `balance` و `name` ذخیره کند.
- یک کلید تصادفی بین `1` تا `9` با `random.randint(1, 9)` تولید و در صفت `password_key` ذخیره کند.
- رمز عبور را با `encrypt()` و همان کلید رمزگذاری و در صفت `password` ذخیره کند؛ متن ساده‌ی رمز نباید ذخیره شود.

```python
account = BankAccount(1000, "Sara", "secret1")
account.balance  # 1000
account.name  # "Sara"
1 <= account.password_key <= 9  # True
account.password == "secret1"  # False
```

#### `get_balance(self, password: str)`

- اگر رمز درست باشد، رشته‌ی `your balance is: <balance>` را برگرداند.
- در غیر این صورت `password is not correct try again` را برگرداند.

```python
account.get_balance("secret1")  # "your balance is: 1000"
account.get_balance("wrong")  # "password is not correct try again"
```

#### `deposit(self, password: str, amount: float | int)`

- اگر رمز درست باشد، مبلغ را به موجودی اضافه کند و رشته‌ی دوخطی `Done\nyour balance is: <balance>` را برگرداند.
- اگر رمز اشتباه باشد، پیام خطا برگرداند و موجودی را تغییر ندهد.

```python
account.deposit("secret1", 500)  # "Done\nyour balance is: 1500"
```

#### `withdraw(self, password: str, amount: float | int)`

- اگر رمز درست باشد و مبلغ از موجودی بیشتر نباشد، مبلغ را کم کند و `your balance is: <balance>` را برگرداند.
- اگر مبلغ از موجودی بیشتر باشد، `your balance is not enough to withdraw` را برگرداند و موجودی را تغییر ندهد.
- اگر رمز اشتباه باشد، پیام خطای رمز را برگرداند.

```python
account.withdraw("secret1", 250)  # "your balance is: 750"
account.withdraw("secret1", 5000)  # "your balance is not enough to withdraw"
```

#### `change_password(self, password: str)`

- اگر رمز درست باشد، رمز جدید را با `input()` بگیرد، کلید تصادفی جدید تولید کند، رمز جدید را با آن رمزگذاری کند و رشته‌ی `Your password has been changed` را برگرداند.
- اگر رمز اشتباه باشد، پیام خطای رمز را برگرداند و رمز فعلی را تغییر ندهد.

```python
account.change_password("secret1")  # "Your password has been changed"
```

#### `account_detail(self, password: str)`

- اگر رمز درست باشد، رشته‌ی دوخطی زیر را برگرداند:

```text
Account owner: <name>
Account Balance: <balance>
```

- در غیر این صورت پیام خطای رمز را برگرداند.

#### `_check_password(self, password: str) -> bool`

این متد کمکی، رمز داده‌شده را با رمزگشایی رمز ذخیره‌شده مقایسه می‌کند و نتیجه را به‌صورت `True` یا `False` برمی‌گرداند. نام آن با زیرخط شروع می‌شود تا مشخص باشد فقط داخل کلاس استفاده می‌شود.

### توابع رمزنگاری

**محل تعریف:** `bank_account/cryptographer.py`

این بخش همان رمز سزار تمرین ۷ است:

- `caesar_cipher(password: str, key: int, decryption: bool = False) -> str`: جابه‌جایی حروف با کلید داده‌شده؛ برای رمزگشایی جهت جابه‌جایی برعکس می‌شود.
- `encrypt(password: str, key: int) -> str`: پوشش ساده‌ای برای رمزگذاری.
- `decrypt(password: str, key: int) -> str`: پوشش ساده‌ای برای رمزگشایی.

نمونه‌ها:

```python
encrypt("secret1", 3)  # "vhfuhw1"
decrypt("vhfuhw1", 3)  # "secret1"
```

### توابع اعتبارسنجی

**محل تعریف:** `bank_account/validator.py`

این توابع به `questionary` داده می‌شوند تا ورودی کاربر پیش از پذیرفته‌شدن بررسی شود:

- `validate_balance(balance: str) -> bool`: با `float()` بررسی می‌کند ورودی عدد باشد و بزرگ‌تر از صفر باشد؛ اگر تبدیل ممکن نباشد `False` برگرداند.
- `validate_name(name: str) -> bool`: طول نام پس از `strip()` باید بیشتر از ۳ باشد.
- `validate_password(password: str) -> bool`: طول رمز پس از `strip()` باید بیشتر از ۶ باشد.

```python
validate_balance("1500")  # True
validate_balance("0")  # False
validate_balance("abc")  # False
validate_name("Sara")  # True
validate_name("Ali")  # False
validate_password("secret1")  # True
validate_password("123456")  # False
```

### `create_account()`

**محل تعریف:** `bank_account/services.py`

الزامات:

- با `questionary.form()` یک فرم سه‌فیلدی با کلیدهای `name`، `balance` و `password` بسازد.
- هر فیلد تابع اعتبارسنجی مناسب خودش را داشته باشد.
- موجودی را با `float()` به عدد تبدیل کند.
- یک شیء `BankAccount` با مقادیر فرم بسازد و برگرداند.

### `main()`

**محل تعریف:** `bank_account/main.py`

الزامات:

- پیام `Welcome to Bank Account` را چاپ کند.
- منوی اول را با `questionary.select()` نمایش دهد و در حالت خروج `So long` برگرداند.
- با انتخاب ساخت حساب، `create_account()` را صدا بزند.
- منوی عملیات را در حلقه‌ی `while True` نمایش دهد.
- با انتخاب گزینه‌ی `2` یا `3`، رمز عبور و مبلغ را بگیرد و مبلغ را با `int()` به عدد تبدیل کند.
- با انتخاب گزینه‌های `1`، `4` یا `5` فقط رمز عبور را بگیرد.
- متد مناسب را از روی دیکشنری `account_transactions` صدا بزند و پیام نتیجه را چاپ کند.
- با انتخاب گزینه‌ی خروج، `have a nice day` برگرداند و برای گزینه‌ی نامعتبر پیام `please select an option` را چاپ کند.

## تست‌های اصلی

فایل‌های تست این تمرین در پوشه‌ی `bank_account/tests/` قرار دارند:

- `test_validator.py`: تست توابع اعتبارسنجی.
- `test_cryptographer.py`: تست توابع رمزگذاری و رمزگشایی.
- `test_account.py`: تست کلاس `BankAccount` و عملیات آن.
- `test_services.py`: تست ساخت حساب از روی فرم.
- `test_main.py`: تست منوها و روند اجرای برنامه.

تست‌های `test_validator.py` این موارد را بررسی می‌کنند:

- `test_validate_balance_accepts_positive_numbers`: قبول اعداد مثبت صحیح و اعشاری، حتی با فاصله‌ی اضافه.
- `test_validate_balance_rejects_zero_and_negative`: رد صفر و اعداد منفی.
- `test_validate_balance_rejects_non_numeric`: رد ورودی خالی، حروف و اعدادی مثل `1,000`.
- `test_validate_name_accepts_names_longer_than_three_characters`: قبول نام‌های بلندتر از سه کاراکتر، حتی با فاصله‌ی ابتدا و انتها.
- `test_validate_name_rejects_short_names`: رد نام‌های سه‌کاراکتری و کوتاه‌تر.
- `test_validate_password_accepts_passwords_longer_than_six_characters`: قبول رمزهای بلندتر از شش کاراکتر.
- `test_validate_password_rejects_short_passwords`: رد رمزهای شش‌کاراکتری و کوتاه‌تر.

تست‌های `test_cryptographer.py` این موارد را بررسی می‌کنند:

- `test_encrypt`: رمزگذاری حروف کوچک و بزرگ، کاراکترهای غیرحرفی و کلیدهای بزرگ‌تر از ۲۶.
- `test_decrypt`: رمزگشایی متن‌های رمزگذاری‌شده و حالت‌های مرزی مثل کلید `0` و `26`.
- `test_decrypt_reverses_encrypt`: بازگشت متن اصلی با رمزگشایی خروجی رمزگذاری، برای کلیدهای مثبت، منفی و بزرگ.
- `test_non_letter_characters_are_preserved`: بدون تغییر ماندن فاصله، عدد و علامت‌ها.
- `test_case_is_preserved`: حفظ بزرگ یا کوچک بودن هر حرف.
- `test_negative_key_shifts_backwards`: پشتیبانی از کلید منفی.
- `test_empty_text`: رفتار درست با رشته‌ی خالی.
- `test_caesar_cipher_decryption_flag`: عملکرد پارامتر `decryption`.
- `test_key_multiple_of_alphabet_returns_same_text`: بدون تغییر ماندن متن وقتی کلید مضربی از ۲۶ است.

تست‌های `test_account.py` این موارد را بررسی می‌کنند:

- `test_account_stores_balance_and_name`: ذخیره‌ی درست موجودی و نام در سازنده.
- `test_account_generates_a_key_between_one_and_nine`: کلید رمز همیشه در بازه‌ی `1` تا `9` است.
- `test_account_stores_password_encrypted`: رمز عبور به‌صورت متن ساده ذخیره نمی‌شود و با کلید حساب قابل رمزگشایی است.
- `test_get_balance_returns_balance_with_correct_password`: بازگشت موجودی با رمز درست.
- `test_get_balance_works_for_float_balance`: کارکرد درست با موجودی اعشاری.
- `test_password_is_case_sensitive`: حساس بودن رمز عبور به بزرگی و کوچکی حروف.
- `test_wrong_password_is_rejected`: برگرداندن پیام خطا و بدون تغییر ماندن موجودی در همه‌ی پنج عملیات، وقتی رمز اشتباه است. این تست پارامتری است و هر پنج متد را جداگانه بررسی می‌کند.
- `test_withdraw_decreases_balance`: کم‌شدن موجودی به اندازه‌ی مبلغ برداشت.
- `test_withdraw_all_balance`: برداشت کل موجودی و رسیدن موجودی به صفر.
- `test_withdraw_more_than_balance_is_rejected`: پیام خطا و بدون تغییر ماندن موجودی در برداشت بیش از موجودی.
- `test_deposit_increases_balance`: افزایش موجودی و پیام `Done`.
- `test_deposit_accepts_float_amount`: پشتیبانی از مبلغ اعشاری در واریز.
- `test_account_detail_shows_owner_and_balance`: خروجی دوخطی نام و موجودی.
- `test_change_password_updates_password`: کارکردن رمز جدید و کار نکردن رمز قبلی بعد از تغییر رمز.
- `test_change_password_re_encrypts_new_password`: ذخیره‌ی رمز جدید به‌صورت رمزگذاری‌شده.

تست‌های `test_services.py` این موارد را بررسی می‌کنند:

- `test_create_account_returns_bank_account`: خروجی `create_account()` از نوع `BankAccount` است.
- `test_create_account_uses_form_values`: نام و رمز از فرم خوانده می‌شوند و ورود با رمز فرم کار می‌کند.
- `test_create_account_converts_balance_to_float`: موجودی خوانده‌شده از فرم به `float` تبدیل می‌شود.
- `test_create_account_asks_for_three_fields`: فرم دقیقاً سه فیلد `name`، `balance` و `password` دارد.

تست‌های `test_main.py` این موارد را بررسی می‌کنند:

- `test_main_prints_welcome_message`: چاپ پیام خوشامدگویی.
- `test_main_returns_so_long_when_exiting_from_welcome_menu`: بازگشت `So long` با خروج از منوی اول.
- `test_main_returns_nice_day_when_exiting`: بازگشت `have a nice day` با خروج از منوی عملیات.
- `test_main_get_balance`: نمایش موجودی پس از وارد کردن رمز درست.
- `test_main_deposit`: واریز مبلغ و افزایش موجودی حساب.
- `test_main_withdraw`: برداشت مبلغ و کاهش موجودی حساب.
- `test_main_withdraw_more_than_balance`: نمایش پیام کافی نبودن موجودی.
- `test_main_change_password`: تغییر رمز از منو و کارکردن رمز جدید.
- `test_main_account_detail`: نمایش نام صاحب حساب و موجودی.
- `test_main_shows_password_error`: نمایش پیام خطا برای رمز اشتباه.
- `test_main_rejects_unknown_option`: پیام `please select an option` برای گزینه‌ی نامعتبر.
- `test_main_applies_multiple_transactions`: انجام چند عملیات پشت‌سرهم و درست ماندن موجودی نهایی.

### اجرای تست‌ها

دستورها را از ریشه‌ی پروژه، یعنی پوشه‌ای که فایل `pyproject.toml` در آن قرار دارد، اجرا کنید.

اجرای تست‌های این تمرین:

```bash
uv run pytest src/009_bank_account -v
```

اجرای یک فایل تست مشخص:

```bash
uv run pytest src/009_bank_account/bank_account/tests/test_account.py -v
```

اجرای همه‌ی تست‌های پروژه:

```bash
uv run pytest
```

## مفاهیم مورد استفاده

- تعریف کلاس با `class` و ساخت شیء
- متد `__init__` و پارامتر `self`
- صفت‌های نمونه (attribute) و متدهای کلاس
- متد خصوصی با پیشوند `_`
- ماژول‌ها و `import` نسبی
- تولید عدد تصادفی با `random.randint()`
- رمز سزار با `ord()`، `chr()` و عملگر باقی‌مانده (`%`)
- ذخیره‌کردن داده به‌صورت رمزگذاری‌شده به‌جای متن ساده
- دیکشنری برای نگاشت گزینه‌های منو به متدها
- دستور `match`/`case` و الگوهای `|`
- حلقه‌ی `while True` و `return` برای خروج از برنامه
- دریافت ورودی با `input()` و کتابخانه‌ی `questionary`
- اعتبارسنجی ورودی و مدیریت خطای `ValueError`
- تبدیل نوع با `float()` و `int()`
- قالب‌بندی رشته با `f-string`
- شرط `if __name__ == "__main__"`
- تست‌نویسی با `pytest`
- استفاده از fixture برای ساخت حساب آماده
- استفاده از `pytest.mark.parametrize`
- شبیه‌سازی `builtins.input` با `monkeypatch`
- جایگزین کردن منوهای `questionary` با پاسخ‌های آماده در تست
- بررسی خروجی چاپ‌شده با `capsys`

## نکته مهم

پیام‌های انگلیسی برنامه بخشی از قرارداد تست‌ها هستند. اگر متن پیام‌ها یا نام متدها را تغییر دهید، تست‌ها شکست می‌خورند. برای مثال پیام رمز اشتباه در همه‌ی متدها دقیقاً `password is not correct try again` است.

کلید رمزگذاری در هر ساخت حساب به‌صورت تصادفی انتخاب می‌شود؛ بنابراین تست‌ها مقدار رمزگذاری‌شده‌ی ثابتی را انتظار ندارند. در عوض بررسی می‌کنند که:

- رمز ذخیره‌شده با متن ساده یکسان نباشد.
- رمز ذخیره‌شده با کلید همان حساب قابل رمزگشایی و برابر رمز اصلی باشد.

اجرای برنامه به ترمینال واقعی نیاز دارد، چون `questionary` منوهای تعاملی می‌سازد. تست‌ها اما منوها را با پاسخ‌های آماده جایگزین می‌کنند، پس در محیط‌های بدون ترمینال هم بدون مشکل اجرا می‌شوند:

```bash
cd src/009_bank_account
uv run python -m bank_account.main
```

اجرای کامل تست‌های این تمرین در حال حاضر ۹۷ تست را با موفقیت پاس می‌کند:

```text
97 passed
```
