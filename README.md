### Step to produce
```
poetry init
poetry install
poetry shell
python -m pytest test.py

```

### Error

_______________________ ERROR at setup of test_something _______________________
ScopeMismatch: You tried to access the 'function' scoped fixture 'faker' with a 'module' scoped request object, involved factories
test.py:5:  def dumb_fixture(faker: faker.proxy.Faker)

### Expected
As documentation labeled: 
https://faker.readthedocs.io/en/master/pytest-fixtures.html

`the faker fixture returns a session-scoped Faker instance to be used across all tests in your test suite`
But The error say it has 'function' scope instead.
^ This is confusing...