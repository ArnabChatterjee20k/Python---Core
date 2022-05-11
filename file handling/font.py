import fontstyle

# format text
text = fontstyle.apply('GEEKSFORGEEKS', 'bold/Italic/red/GREEN_BG')

# display text
print(text)

# display formatted text
print(fontstyle.apply('GEEKSFORGEEKS',
                      'bold/Italic/red/UNDERLINE/GREEN_BG'))

print(fontstyle.apply('GEEKSFORGEEKS',
                      'bold/Italic/red/INVERSE/UNDERLINE/GREEN_BG'))

# apply formatting
text = fontstyle.apply(
    'GEEKSFORGEEKS', 'bold/Italic/blink/green/INVERSE/2UNDERLINE/strike/Red_BG')

# display text
print(text)

# preserved text
print(fontstyle.preserve(text))

choice.a=input(fontstyle.apply("1)Add\n2)Remove\n3)View\n4)Update","bold/underline/red"))
print(choice.a)

