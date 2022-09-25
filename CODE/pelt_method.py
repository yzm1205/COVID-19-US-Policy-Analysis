import rupture as rpt


bp = {}
def breakpoints(data,state = ""):
    model='rbf'
    X = data[f"{state}_cases"].values
    algo = rpt.Pelt(model=model).fit(X)
    result = algo.predict(pen=10)
    bp[state] = result
    # rpt.display(X,result,figsize=(8,3))
    # [plt.axvline(x) for x in range(len(6))]  # Include policy day in bp graph. *Later
    # plt.title(f"{state} Confirmed Cases")
    # plt.show()