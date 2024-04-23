import pandas as pd
from tabulate import tabulate


def write_report(Report_file, title):
        Report_file.write(f'### Write an example of MD file using Python {title} \n\n')

        data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [28, 25, 32],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

        df = pd.DataFrame(data)

        markdown_table = tabulate(df, headers='keys', tablefmt='github', showindex=False)

        Report_file.write(markdown_table)


if __name__ == "__main__": 
    value = 5
    with open(f'example.MD', 'w') as rep_f:
        rep_f.write(f'# Generated a MD file {value} version \n\n')
        write_report(rep_f, title='v3.10')
        rep_f.write(f'\n\n')
        

