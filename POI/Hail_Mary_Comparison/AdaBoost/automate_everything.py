import itertools
import subprocess
import sys

def main():
  attributes_possible = ["salary", "bonus", "expenses", "frac_from_poi", "frac_all", "frac_to_poi", "shared_receipt_with_poi", "exercised_stock_options"]
  features = list(itertools.combinations(attributes_possible, 4))

  """
  calling the boosting algorithm
  """  
  """
    The outermost loop runs through all possible feature combinations
    The outerloop runs through the number of estimators. (Move granularly from 5 to 5000)
    The inner loop varies the learning rate. The learning rate in a ADA Boost Algorithm affects the    weighted average calculation. (Move granularly from 0.1 to 3.0 with steps of 0.05)
  """
  for feature in features:
    for num in range(1, 5001, 100):
      for lr in range(10, 300, 10):
        lr *= 0.01
        subprocess.call(["python", "starter_ada.py", str(num), str(lr), " ".join(feature)])
        for fold in range(2, 5):
          subprocess.call(["python", "ada.py", str(num), str(lr), str(fold), " ".join(feature)])  
    
      

if __name__ == "__main__":
  main()
