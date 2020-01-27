create_expense = '''mutation{{
  createExpense(name: "{name}", amount: {amount}){{
    expense{{
      name
      amount
    }}
    message
  }}
}}'''

get_my_expenses = '''{
  myExpenses{
    id
    name
  }
}'''

update_expense = '''
mutation{{
  updateExpense(id:"{id}", description: "{description}",
  name: "{name}", amount: {amount}){{
    updated{{
      name
      description
      amount
    }}
    message
  }}
}}
'''
