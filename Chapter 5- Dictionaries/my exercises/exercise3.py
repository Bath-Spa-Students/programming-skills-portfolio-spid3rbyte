glossary = {
    'comment':'comments help the user with code',
    'float': 'float converts numbers to decimal points',
    'integer': 'integer helps numbers stay as a whole number',
    'string': "a collection of alphabets and numbers",
    'print': "command to print a specific message to the screen",
    'boolean':"boolean represents either true or false",
    'if':"used to check a condition",
    'input':"lets the user input values",
    'type':"checks the data type",
    'append':"allows user to add a value to the list",
}
for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)