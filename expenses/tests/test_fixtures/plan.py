create_plan = '''
mutation{{
createPlan(name: "{name}",
    amount: {amount},
    dueDate: "{dueDate}",
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
