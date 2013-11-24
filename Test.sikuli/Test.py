def testUKSchedule():
    click("1385334170517.png")
    type("www.ukathletics.com/\n")
    hover("1385334251922.png")
    click(Pattern("1385334347646.png").targetOffset(-6,17))
    assert (find("1385334444640.png").exists("1385335665825.png"))

testUKSchedule()
    
    
    