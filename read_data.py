import wfdb
import pandas as pd
import csv

#record = wfdb.rdsamp('ecg_data/100', sampto = 3000)
#annotation = wfdb.rdann('ecg_data/100', 'atr', sampto = 3000)


def main():
    ecgrecord  = wfdb.rdsamp('ecg_data/100', sampfrom=0, sampto = 5000)
    annotation = wfdb.rdann('ecg_data/100', 'atr', sampto = 5000)

    #print(len(ecgrecord.p_signals))

    print(ecgrecord.p_signals[0])
    print(ecgrecord.p_signals[0][0])
    print(ecgrecord.p_signals[0][1])


    wfdb.plotrec(ecgrecord, annotation = annotation, title='Record 100 from MIT-BIH Arrhythmia Database', timeunits = 'seconds', figsize = (10,4), ecggrids = 'all')

if __name__ == "__main__":
    main()