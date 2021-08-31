# Deposit Plan

[![Run on Repl.it](https://repl.it/badge/github/VishalTaj/deposit_plan)](https://repl.it/github/VishalTaj/deposit_plan)

## Table of Contents
<!-- TOC depthFrom:1 depthTo:6 withLinks:1 orderedList:0 -->
- [Approach](#approach)
- [Directory Strcuture](#directory-structure)
- [Running Test Case](#running-test-case)
- [Scope](#scope)
   - [User Story](#user-story)
   - [Actions](#actions)
   - [Ratio Calculation](#ratio-calculation)
   - [Schema](#schema)
<!-- /TOC -->

## Approach

I have followed TDD approach to get to a solution.

in order to make customers reference code unique i have used md5(email, name). 

There are 2 types of Deposit plans in this application:

#### OneTime Plan:

will only execute once and in order to be successfull the customer must deposit the exact amount of money to the portfolio.

#### Monthly Plan:

This will be a recurring plan so the customer can deposit the amount monthly.

> Once customer reaches target amount portfolio will be credited with the amount. a flag will be set to true to indicate that the plan has reached the target.


## Directory Structure

```directory
|-- deposit_plan
|   |-- config
|   |   |-- exception.py
|-- |-- customer
|   |   |-- customer.py
|   |   |-- portfolio.py
|   |   |-- __init__.py
|-- |-- deposit
|   |   |-- deposit_plan.py
|   |   |-- __init__.py
```

### Running Test case

```bash
$ python3 test_sample.py
```

## Scope

Below is my findings and assumptions about the problem.

### User Story

- As a Customer i will have a unique Reference code to do all operations
- As a Customer i can create max of 2 unique Deposit Plan with portfolio
- As a Customer i can deposit fund via bank transfer to my portfolio

### Actions:

- Create Customer
- Create Deposit Plan with respective portfolio
plan types either one time or reccuring/monthly
can specify the percentage or ratio of amount to be deposited per portfolio
- Start depositing
update portfolio with deposit amount


### Ratio calculation:

Once we created a deposit plan we will have to calculate the ratio of the amount to be credited to each portfolio. 

for finding ratio

```
x_ratio = x / x + y
y_ratio = y / x + y
```

when the customer deposit an amount we will use this ratio to allocate the amount to each portfolio.

allocation of amount based on ratio

```
portfolio_1 = (x_ratio / x_ratio + y_ratio) * deposited_amount
portfolio_2 = (y_ratio / x_ratio + y_ratio) * deposited_amount
```


### Schema

```
Customer:
    - name: string
    - email: string
    - age: int
    - reference_code: md5(email, name)
    - deposit_plans: [DepositPlan]
```

```
Portfolio:
    - reference_code: customer_reference_code
    - name: string
```

```
DepositPlan:
    - reference_code: customer_reference_code
    - portfolios: [Portfolio]
    - recurring: boolean, default: false
```




