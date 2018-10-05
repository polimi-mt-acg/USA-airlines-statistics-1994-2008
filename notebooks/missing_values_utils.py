from pathlib import Path
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


def get_df_missing_and_drop_all_null(df, do_computation, missing_dataframe_path):
    # drop nulls
    if Path(missing_dataframe_path).is_file() and not do_computation:
        # load from cache
        df_missing = pd.read_pickle(missing_dataframe_path)
    else:
        df_years = range(1994, 2009)
        print("Years examined:\n", list(df_years))

        # do inspection
        print("\nMissing values inspection:")
        for c in df.columns:
            print(df.filter(df[c].isNull()).count(), " null values in: ", c)

        # calculate missing per year
        counts = []
        for y in df_years:
            counts.append(df.filter(df.Year == y).count())

        df = df.dropna()

        counts_after = []
        for y in df_years:
            counts_after.append(df.filter(df.Year == y).count())

        df_missing = pd.DataFrame({'Count': counts, 'CountAfterDrop': counts_after}, index=df_years)

        df_missing['MissingsCount'] = df_missing['Count'] - df_missing['CountAfterDrop']
        df_missing.drop('CountAfterDrop', 'columns', inplace=True)
        df_missing['MissingsPercentage'] = df_missing['MissingsCount'] / df_missing['Count']

        # cache it
        df_missing.to_pickle(missing_dataframe_path)
        print("\n")

    print(df_missing)
    return (df, df_missing)


def plot_missing_values_stacked_bar(df_missing):
    plt.rcParams.update({'figure.figsize': (22, 12)})
    plt.rcParams.update({'font.size': 20})

    ax = plt.figure().add_subplot(111)

    patch_handles = []

    total = 0
    total_missing = 0
    for year, r in df_missing.iterrows():
        total += r['Count']
        total_missing += r['MissingsCount']
        percentages = [
            (1 - r['MissingsPercentage']) *100,
            r['MissingsPercentage'] *100
        ]
        height = percentages
        bottom = [0, height[0]]

        patch_handles.append(
            ax.bar(year, height=height, align='center', bottom=bottom, color=['#00aa00', '#ff0000'])
        )
        for i, patch in enumerate(patch_handles[-1]):
            bl = patch.get_xy()
            x = 0.5 * patch.get_width() + bl[0]
            y = 0.5 * patch.get_height() + bl[1]
            ax.text(x, y, "{0:.1f}%".format(round(percentages[i], 2)), ha='center', va='center', color='w', size=16)

    years = list(df_missing.index)

    x_pos = range(years[0], years[-1] + 1)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(years, size=16)
    ax.set_xlabel('Year')
    ax.set_ylabel('Percentage')

    total = int(total)
    total_missing = int(total_missing)
    legend_elements = [
        matplotlib.lines.Line2D([0], [0], color='#ffffff', lw=4,
                                label='Total data.....................................{:,} rows'.format(total)),
        matplotlib.lines.Line2D([0], [0], color='#ff3232', lw=4,
                                label='Excluded due to missing values...{:,} rows'.format(total_missing)),
        matplotlib.lines.Line2D([0], [0], color='#00bb22', lw=4,
                                label='Valid data used in analytics.........{:,} rows'.format(total - total_missing))
    ]

    ax.legend(handles=legend_elements, loc="center", bbox_to_anchor=(0.5, -0.2))
    ax.set_title('Used valid data   vs.  Excluded data due to missing values', pad=20)
    plt.xlim(xmin=1993.5, xmax=2008.5)
    plt.show()

    # reset to default rcParams
    plt.rcParams.update(plt.rcParamsDefault)

	
