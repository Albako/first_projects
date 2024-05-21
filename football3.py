import os
import pandas as pd
import matplotlib.pyplot as plt

current_folder = os.getcwd()
file_path = os.path.join(current_folder, 'match_results.txt')


class FootballData:
    """
    A class used to represent football data from a txt file.

    Attributes
    ----------
    data : list. List of strings.
    teams_and_scores : list. List of lists.
    scores : list. List of strings.

    Static Methods
    -------
    load_data(file_path : str) -> list
    split_strings_in_iterable(iterable : list, split_char : str) -> list
    get_given_elem_of_each_iterab_in_nested_iterab(iterable : list, idx : int = - 1) -> list
    """

    # 1. tutaj wklej kod odpowiadajacy za
    # wczytanie danych z pliku i przeksztalc
    # go na metode/funkcje/metode statyczna

    def load_data(inp_file_path: str) -> list:
        return open(inp_file_path, 'r').readlines()

    # 2. tutaj wklej kod funkcji ktora rozbija stringi (lancuchy)
    # w liscie i zamien ja na metode/metode statyczna
    def split_strings_in_iterable(iterable: list, split_char: str) -> list:
        """
        Splits strings in an iterable by a given character
        and returns a list of lists.

        Parameters
        ----------
        iterable : list. List of strings.
        split_char : str. Character to split by.

        Returns
        -------
        list.

        Example
        -------
        split_strings_in_iterable( [ 'Southern Dynamo:Northern Rangers,3-0\n', 'FC Stars:Southern Galaxy,4-0\n' ], ',' )

            [ [ 'Southern Dynamo:Northern Rangers', '3-0\n' ], [ 'FC Stars:Southern Galaxy', '4-0\n' ] ]

        """
        return [i.split(split_char) for i in iterable]

    # 3. tutaj wklej kod funkcji ktora z kazdej listy w
    # liscie list (nested iterab) pobiera okreslony element i
    # zwraca plaska liste, a nastepnie zamien ja na metode/metode statyczna
    def get_given_elem_of_each_iterab_in_nested_iterab(iterable: list, \
                                                       idx: int = - 1) -> list:
        """
        Returns the last element of each list in a nested list.

        Parameters
        ----------
        iterable : list. List of lists.

        Returns
        -------
        list. Flat list of the last elements of each list in the nested list.

        Example
        -------
        get_last_elem_of_each_iterab_in_nested_iterab( [ [ 'Southern Dynamo:Northern Rangers', '3-0\n' ], [ 'FC Stars:Southern Galaxy', '4-0\n' ] ] )

            [ '3-0\n', '4-0\n' ]
        """

        return [i[idx] for i in iterable]

    def __init__(self, file_path):
        self.data = FootballData.load_data(file_path)
        self.teams_and_scores = FootballData \
            .split_strings_in_iterable(self.data, \
                                       split_char=',')
        self.scores = FootballData \
            .get_given_elem_of_each_iterab_in_nested_iterab( \
            self.teams_and_scores)


class FootballDataPreprocessing(FootballData):
    """
    A class describing processing of football scores data.

    Attributes
    ----------
    file_path : str.
    data : list. List of strings.
    teams_and_scores : list. List of lists.
    scores : list. List of strings.
    scores_no_whitespace : list. List of strings.

    Methods
    -------
    extract_scores(which_side : str = 'H') -> list
    """

    def __init__(self, file_path):
        super().__init__(file_path)
        self.scores_no_whitespace = [s.strip() for s in self.scores]

    def extract_scores(self, which_side='H'):
        idx = 0

        if which_side == 'A':
            idx = 1

        scores = [int(s.split('-')[idx]) for s in \
                  self.scores_no_whitespace]

        return scores


class FootballDataAnalytics(FootballDataPreprocessing):
    """
    A class for analyzing football scores data.

    Attributes
    ----------
    file_path : str.
    data : list. List of strings.
    teams_and_scores : list. List of lists.
    scores : list. List of strings.
    scores_no_whitespace : list. List of strings.
    home_scores : list. List of integers.
    away_scores : list. List of integers.
    outcomes : list. List of strings.

    Methods
    -------
    get_counts_of_outcomes() -> pd.Series
    plot_counts_of_outcomes()

    Static Methods
    -------
    calc_outcome(homescore : int, away_score : int) -> str"""

    # 4. tutaj wklej kod funkcji ktora na podstawie ilosci
    # goli strzelonych przez gospodarzy i druzyne przyjezdna
    # mowi kto wygral mecz
    # a nastepnie zamien ja na metode/metode statyczna
    def calc_outcome(homescore: int, away_score: int):
        """
        Takes the number of goals scored by home and
        away teams and based on that calculates
        the outcome 'H' (home win) / 'D' (draw) / 'A' (away win).

        Parameters
        ----------
        homescore : int.
        away_score : int.

        Returns
        -------
        str.

        Examples
        -------
        calc_outcome(2, 1)

            'H'

        calc_outcome(1, 2)

            'A'

        calc_outcome(1, 1)

            'D'

        calc_outcome(3, 4)

            'A'
        """
        # to determine if the home team scored
        # more goals and therefore won
        if homescore > away_score:
            return 'H'
        # to check whether away team scored more goals
        # which would make them winners
        elif homescore < away_score:
            return 'A'
        # to find out if both teams
        # scored the same number of goals
        # which would indicate a draw
        elif homescore == away_score:
            return 'D'

    def __init__(self, file_path):
        super().__init__(file_path)
        self.home_scores = self.extract_scores(which_side='H')
        # 5. tutaj oblicz wyniki druzyn przyjezdnych
        self.away_scores = self.extract_scores(which_side='A')
        self.outcomes = [FootballDataAnalytics \
                             .calc_outcome(h, a) for h, a in zip( \
            self.home_scores, self.away_scores)]

    # 7. 2 linijki wyzej zamien odpowiednia_metoda na nazwe metody, ktora
    # pozwala ustalic wynik meczu

    def get_counts_of_outcomes(self):
        # 8. dostosuj ponizsza linijke kodu wstawiajac cos zamiast '???'
        # ta metoda liczy czestosc poszczegolnych wynikow meczow
        return pd.Series(self.outcomes).value_counts()

    def plot_counts_of_outcomes(self):
        self.get_counts_of_outcomes().plot.bar()
        plt.title('Distribution of football games outcomes')
        plt.xlabel('Outcome', labelpad=10)
        plt.ylabel('Count')
        plt.show()


print(FootballDataAnalytics(file_path).plot_counts_of_outcomes())