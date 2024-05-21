import os
import pandas as pd
import matplotlib.pyplot as plt

class FootballData:
    @staticmethod
    def load_data(file_path: str) -> list:
        with open(file_path, 'r') as f:
            return f.readlines()

    @staticmethod
    def split_strings_in_iterable(iterable: list, split_char: str) -> list:
        return [i.split(split_char) for i in iterable]

    @staticmethod
    def get_given_elem_of_each_iterab_in_nested_iterab(iterable: list, idx: int = -1) -> list:
        return [i[idx] for i in iterable]

    def __init__(self, file_path):
        self.data = self.load_data(file_path)
        self.teams_and_scores = self.split_strings_in_iterable(self.data, ',')
        self.scores = self.get_given_elem_of_each_iterab_in_nested_iterab(self.teams_and_scores)


class FootballDataPreprocessing(FootballData):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.scores_no_whitespace = [s.strip() for s in self.scores]

    def extract_scores(self, which_side='H'):
        idx = 0 if which_side == 'H' else 1
        return [int(s.split('-')[idx]) for s in self.scores_no_whitespace]


class FootballDataAnalytics(FootballDataPreprocessing):
    @staticmethod
    def calc_outcome(homescore: int, away_score: int) -> str:
        if homescore > away_score:
            return 'H'
        elif homescore < away_score:
            return 'A'
        elif homescore == away_score:
            return 'D'

    def __init__(self, file_path):
        super().__init__(file_path)
        self.home_scores = self.extract_scores(which_side='H')
        self.away_scores = self.extract_scores(which_side='A')
        self.outcomes = [self.calc_outcome(h, a) for h, a in zip(self.home_scores, self.away_scores)]

    def get_counts_of_outcomes(self) -> pd.Series:
        return pd.Series(self.outcomes).value_counts()

    def plot_counts_of_outcomes(self):
        print("blabla")
        self.get_counts_of_outcomes().plot.bar()
        plt.title('Distribution of football games outcomes')
        plt.xlabel('Outcome', labelpad=10)
        plt.ylabel('Count')
        plt.show()


file_path = os.path.join(os.getcwd(), 'match_results.txt')
FootballDataAnalytics(file_path).plot_counts_of_outcomes()
