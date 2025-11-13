from pyscript import display 

math_club={'Clarisse', 'Yvonne', 'Franzeska', 'Addienna', 'Lia', 'Isabel'}
monarchs={'Ashley', 'Rose', 'Erich', 'Jasmine', 'Lia', 'Isabel'}

display(math_club | monarchs, target='output')
display(math_club & monarchs, target='output')
display(math_club - monarchs, target='output')
display(monarchs - math_club, target='output')
display(monarchs ^ math_club, target='output')
