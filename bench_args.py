import timeit
from statistics import mean
import modules.p_funcs as pfuncs
import c_funcs as cfuncs


def return_arg(val=1):
    return val


def return_1():
    return 1


def main():
    da_scores = []
    nda_scores = []
    na_scores = []

    eda_scores = []
    enda_scores = []
    ena_scores = []

    cda_scores = []
    cnda_scores = []
    cna_scores = []

    total_attempts = 10
    loops_per_attempt = 10000000
    for i in range(total_attempts):
        print('attempt:', i + 1)
        print('stage1: functions in the internal file')
        da_score = timeit.timeit('return_arg()', number=loops_per_attempt, globals=globals())
        da_scores.append(da_score)

        print('elapsed time for calling method with a default argument 10M times: {:.3f} sec'.format(da_score))

        nda_score = timeit.timeit('return_arg(2)', number=loops_per_attempt, globals=globals())
        nda_scores.append(nda_score)

        print('elapsed time for calling method with a non-default argument 10M times: {:.3f} sec'.format(nda_score))

        na_score = timeit.timeit('return_1()', number=loops_per_attempt, globals=globals())
        na_scores.append(na_score)

        print('elapsed time for calling method without getting argument 10M times: {:.3f} sec'.format(na_score))

        print('stage2: functions in the external file')
        eda_score = timeit.timeit('pfuncs.return_arg()', number=loops_per_attempt, globals=globals())
        eda_scores.append(eda_score)

        print('elapsed time for calling method with a default argument 10M times: {:.3f} sec'.format(eda_score))

        enda_score = timeit.timeit('pfuncs.return_arg(2)', number=loops_per_attempt, globals=globals())
        enda_scores.append(enda_score)

        print('elapsed time for calling method with a non-default argument 10M times: {:.3f} sec'.format(enda_score))

        ena_score = timeit.timeit('pfuncs.return_1()', number=loops_per_attempt, globals=globals())
        ena_scores.append(ena_score)

        print('elapsed time for calling method without getting argument 10M times: {:.3f} sec'.format(ena_score))

        print('stage3: functions written in Cython')
        cda_score = timeit.timeit('cfuncs.return_arg()', number=loops_per_attempt, globals=globals())
        cda_scores.append(cda_score)

        print('elapsed time for calling method with a default argument 10M times: {:.3f} sec'.format(cda_score))

        cnda_score = timeit.timeit('cfuncs.return_arg(2)', number=loops_per_attempt, globals=globals())
        cnda_scores.append(cnda_score)

        print('elapsed time for calling method with a non-default argument 10M times: {:.3f} sec'.format(cnda_score))

        cna_score = timeit.timeit('cfuncs.return_1()', number=loops_per_attempt, globals=globals())
        cna_scores.append(cna_score)

        print('elapsed time for calling method without getting argument 10M times: {:.3f} sec'.format(cna_score))

    print('stage1 results:')
    print('average time for calling method with a default argument: {} sec'.format(mean(da_scores)))
    print('average time for calling method with a non-default argument: {} sec'.format(mean(nda_scores)))
    print('average time for calling method without getting argument: {} sec'.format(mean(na_scores)))
    print('stage2 results:')
    print('average time for calling method with a default argument: {} sec'.format(mean(eda_scores)))
    print('average time for calling method with a non-default argument: {} sec'.format(mean(enda_scores)))
    print('average time for calling method without getting argument: {} sec'.format(mean(ena_scores)))
    print('stage3 results:')
    print('average time for calling method with a default argument: {} sec'.format(mean(cda_scores)))
    print('average time for calling method with a non-default argument: {} sec'.format(mean(cnda_scores)))
    print('average time for calling method without getting argument: {} sec'.format(mean(cna_scores)))


if __name__ == "__main__":
    main()
