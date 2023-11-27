def main():
    female = int(input('Enter the number of female students:'))
    male = int(input('Enter the number of male students:'))
    total = female + male 
    f_per = female * 100 / total 
    m_per = male * 100 / total

    print(f'Female Percentage is:\t{f_per:.2f}')
    print(f'Male Percentage is: \t{m_per:.2f} ')
    
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
