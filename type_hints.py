price = 100
tax = 1.1

def calc_price__including_tax(price: int, tax: float) -> int:
  return int(price * tax)

if __name__ == '__main__':
  print(f'{calc_price__including_tax(price, tax)}円')