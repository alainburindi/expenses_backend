create_plan = '''
mutation{{
createPlan(name: "{name}",
    amount: {amount},
    dueDate: "{due_date}",
    description: "{description}"
){{
    plan{{
      amount
      name
      description
    }}
    message
  }}
}}
'''

update_plan = '''
mutation{{
  updatePlan(id: "{id}", name: "{name}",
  amount: {amount}, dueDate: "{due_date}"){{
    plan{{
      name
      description
      amount
      dueDate
    }}
    message
  }}
}}
'''

delete = '''
mutation{{
  deletePlan(ids: {}){{
    message
    failed
  }}
}}
'''
