import itertools
import subprocess
import sys

def main():
  attributes_possible = ["salary", "bonus", "expenses", "frac_from_poi", "frac_all", "frac_to_poi", "shared_receipt_with_poi", "exercised_stock_options"]
  features = list(itertools.combinations(attributes_possible, 4))

  "Outerloop is going to vary number of estimators"
  "Inner loop is going to vary k for cross validation"

  for feature in features:
    for num in range(5, 5000):
      subprocess.call(["python", "bagging_starter.py", str(num), " ".join(feature)])
      for fold in range(2, 5):
        subprocess.call(["python", "bagging.py", str(fold), str(num), " ".join(feature)])

if __name__ == "__main__":
  main()
