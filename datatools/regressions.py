from abc import ABC

import statsmodels.api as sm
from statsmodels.stats.outliers_influence import summary_table


class RegressionsBase(ABC):
    pass

    def linear_regression(self, x, y):
        pass

class StatsModelsRegressions(RegressionsBase):
    def linear_regression(self, x, y):
        x = sm.add_constant(x)
        regr = sm.OLS(y, x)
        res = regr.fit()
        # Get fitted values from model to plot
        st, data, ss2 = summary_table(res, alpha=0.05)
        fitted_values = data[:,2]
        return fitted_values
