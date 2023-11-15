sandwich_orders = ['turkey sandwich', 'shawarma', 'egg sandwich', 'chicken sandwich', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("no more pastrami left")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    made_sandwiches = sandwich_orders.pop()
    print("Your " + made_sandwiches + " is being made")
    finished_sandwiches.append('turkey sandwich')
    finished_sandwiches.append('shawarma')
    finished_sandwiches.append('egg sandwich')
    finished_sandwiches.append('chicken sandwich')

for sandwich in finished_sandwiches:
    print("Your " + sandwich + " is done being made")