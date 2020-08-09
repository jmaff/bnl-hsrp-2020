import dft
import cf
import matplotlib.pyplot as plt

a0 = [13,17,17,19,13,13,19,1,19,7,5,19,17,17,19,19,5,19,19,17,19,19,2,19,2,13,17,19,19,11,11,19,1,13,19,1,17,13,2,5,19,17,17,11,2,13,7,5,3,5,13]
b0 = [13,11,17,19,13,17,7,2,17,11,11,19,17,17,13,17,17,19,11,11,17,5,11,11,7,7,7,5,17,7,17,5,13,13,2,17,5,13,19,19,11,13,7,2,17,13,17,5,11,11,11]
a = [-13,-5,-7,0,-7,-5,-11,-11,-17,-2,-17,-7,-2,-19,-2,-1,-2,-13,0,7,-11,-7,-7,-11,-2,-3,-2,-1,-17,-1,-5,-2,1,-11,-17,-1,-2,-7,-1,-1,-5,-3,-11,-5,-1,-1,-11,-2,-1,-1,-5]
b = [13,3,7,-2,-19,0,5,-7,-2,-3,-3,11,-1,13,-11,-17,-19,5,-11,-17,0,-5,11,0,-11,-13,-5,-13,-3,1,5,0,-19,19,13,-11,-5,-2,-11,5,-7,-11,5,-19,-3,-19,-17,-19,-5,-5,-13]
c = [-13,-7,-1,-5,-2,-13,-3,-19,2,-19,-13,19,2,17,0,7,5,-13,2,-7,-11,-13,-19,3,0,-13,-19,-17,-19,-7,17,-13,3,-7,19,-19,-3,-19,-1,-19,-13,-11,-19,-1,-13,-5,-7,-17,-3,-3,-19]
d = [13,5,-11,19,7,13,7,19,13,13,19,-17,3,-11,5,7,5,13,5,2,13,13,5,7,7,7,13,7,11,3,-11,3,3,-7,-11,7,3,7,7,7,13,13,13,7,5,13,19,19,3,3,19]
e = [-1,-1,13,-17,-2,-11,-17,-17,-11,-11,-17,19,-2,13,-2,-5,-1,-11,-3,2,-11,-11,-2,-5,-5,-3,-11,-3,-7,-1,13,1,2,11,13,-3,1,-3,-5,-5,-11,-11,-11,-3,-2,-11,-17,-17,0,0,-17]

titles = ['a0', 'b0', 'a', 'b', 'c', 'd', 'e']
data = [a0, b0, a, b, c, d, e]

if __name__ == '__main__':
    # for i, variable in enumerate(data):
    #     dft_var = dft.dft(variable)
    #     plt.figure(1)
    #     dft.plot_dft(dft_var, (2, 4, i+1), titles[i])
    #
    #     plt.figure(2)
    #     dft.plot_dft_power(dft_var, (2, 4, i + 1), titles[i])
    #
    #     plt.figure(3)
    #     plt.subplot(2, 4, i+1)
    #     plt.plot(variable, '-b', label="Original")
    #     plt.plot(dft.idft(dft_var, 51), ':r', label="IDFT")
    #     plt.legend(loc='upper right')
    #
    # plt.show()

    # for n in range(0, 50):
    #     coeffs = []
    #
    #     for variable in data:
    #         coeffs.append(dft.idft_get(dft.dft(variable), n, 51))
    #
    #     print(f"{n}: " + str(coeffs))

    coeffs = []
    n = 50

    for variable in data:
        coeffs.append(round(dft.idft_get(dft.dft(variable), n - 1, 51)))

    print(cf.hk_decode_to_decimal(cf.hk_quadlin_gen_decode(coeffs[0], coeffs[1], coeffs[2:], 15), 10))
    print(coeffs)
    # print(cf.hk_decode_to_decimal(cf.hk_quadlin_gen_decode(19, 5, [-7, -5, -13, 13, -11], 15), 10))