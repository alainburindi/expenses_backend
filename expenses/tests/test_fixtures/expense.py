create_expense = '''mutation{{
  createExpense(name: "{name}", amount: {amount}){{
    expense{{
      name
      amount
    }}
    message
  }}
}}'''
