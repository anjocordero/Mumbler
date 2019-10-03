def chartSwitcher(chart):
    """
    Choose which billboard chart to search, when given argument in command line

    chartName taken from billboard.com urls
    """

    if chart == "hot100":
        chartName = "hot-100"

    elif chart == "pop":
        chartName = "pop-songs"

    elif chart == "latin":
        chartName = "latin-songs"

    elif chart == "hiphop":
        chartName = "r-b-hip-hop-songs"

    elif chart == "edm":
        chartName = "dance-electronic-songs"

    elif chart == "alternative":
        chartName = "alternative-songs"

    elif chart == "rock":
        chartName = "rock-songs"

    elif chart == "country":
        chartName = "country-songs"

    else:
        print(
            "No genre specified. Try again with [hot100/pop/rock/latin/hiphop/alternative/edm/country].")

    return chartName
