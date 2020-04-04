import numpy as np

def main():
    mean_total_payment(10) # n=10 or 20
    p_total_payment(10) # n=10 or 20

def run(n):
    total_payment = 0
    payment_list = []
    Random_select = []
    Rm = np.random.choice(n,n,replace=False)
    for i in range(n):
        if i == 0:
            current_payment = Rm[i]+1
            total_payment = Rm[i]+1
            payment_list.append(current_payment)
            Random_select.append(Rm[i]+1)
        else:
            privous_payment = Rm[i-1]+1
            current_payment = Rm[i]+1
            x = current_payment-privous_payment
            absolute_difference = np.fabs(x)
            payment_list.append(absolute_difference)
            Random_select.append(Rm[i]+1)
            total_payment = total_payment + absolute_difference
    return total_payment

def mean_total_payment(n):
    result = []
    for i in range(20):
        total_payment = run(n)
        result.append(total_payment/n)
    answer1 = np.sum(result)/20
    print(answer1)
    answer2 = np.std(result)
    print(answer2)

def p_total_payment(n):
    count = 0
    for i in range(1000000):
        total_payment = run(n)
        if total_payment >= 45: #45 or 160
            count = count + 1
    p = count/1000000
    print(p)

if __name__ == '__main__':
    main()