import unittest

def butterfly_sum(num1, num2, denum1, denum2):
    try:
        ans_num=(num1*denum2)+(num2*denum1)
        ans_denum=denum2*denum1
        return [ans_num, ans_denum]
    except:
        ans_num='error'
        ans_denum='error'
        return [ans_num, ans_denum]

def butterfly_substract(num1, num2, denum1, denum2):
    try:
        ans_num=(num1*denum2)-(num2*denum1)
        ans_denum=denum2*denum1
        return [ans_num, ans_denum]
    except:
        ans_num='error'
        ans_denum='error'
        return [ans_num, ans_denum]

class butterfly(unittest.TestCase):
    def setUp(self):
        pass

    def test_bf1(self):
        result = butterfly_sum(1,1,1,1)
        self.assertEqual([2,1], result)

    def test_bf2(self):
        result = butterfly_substract(1,1,1,1)
        self.assertEqual([0,1], result)

    def test_bf3(self):
        result = butterfly_sum(1,1,1,'1')
        self.assertEqual(['error', 'error'], result)

    def test_bf4(self):
        result = butterfly_sum(1,1,1,'')
        self.assertEqual(['error', 'error'], result)

    def test_bf5(self):
        result = butterfly_substract(1,1,1,'1')
        self.assertEqual(['error', 'error'], result)

    def test_bf6(self):
        result = butterfly_substract(1,1,1,'')
        self.assertEqual(['error', 'error'], result)
