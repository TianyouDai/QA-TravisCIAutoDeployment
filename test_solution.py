from solution import Solution
def test_Neg():
    s = Solution()
    assert s.checkPerfectNumber(-2) == False
    
def test_0():
    s = Solution()
    assert s.checkPerfectNumber(0) == False

def test_6():
    s = Solution()
    assert s.checkPerfectNumber(6) == True

def test_28():
    s = Solution()
    assert s.checkPerfectNumber(28) == True

def test_13():
    s = Solution()
    assert s.checkPerfectNumber(13) == False

def test_90():
    s = Solution()
    assert s.checkPerfectNumber(90) == False

def test_86():
    s = Solution()
    assert s.checkPerfectNumber(86) == False
    
def test_2394():
    s = Solution()
    assert s.checkPerfectNumber(2394) == False
