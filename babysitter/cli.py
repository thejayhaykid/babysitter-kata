""" Command Line Interface for the babysitter kata """

import click
from babysitter import Sitter

@click.command()
@click.option('--start','-s',prompt='Start time',help='The time you started babysitting. Format as 24-hour time with no colon. Example: To enter 5PM, put in \'1700\'')
@click.option('--end','-e',prompt='End time',help='The time you stopped babysitting. Format as 24-hour time with no colon. Example: To enter 5PM, put in \'1700\'')
@click.option('--family','-f',prompt='Which family',type=click.Choice(['A','B','C']),help='Select which family you are babysitting for; A, B, or C.')
def main(start, end, family):
    """ Main point of entry for CLI via click """
    main_sitter = Sitter(start_time=start,end_time=end,family=family)
    print(main_sitter.babysit())
