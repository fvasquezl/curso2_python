increment = lambda x: x+1

full_name = lambda name,lastname: f'Full name is {name.title()} {lastname.title()}'


result = increment(10)

print(result)
fn = full_name('faustino', 'Vasquez')

print(fn)