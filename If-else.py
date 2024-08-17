score = int(input("Enter you score"))

if score >= 90:
    print("A grade")
else:
    if score >= 80:
        print("B grade")
    else:
        if score >=70:
            print("C grade")
        else:
            if score >=60:
                print("D grade")
            else:
                print("F grade")
