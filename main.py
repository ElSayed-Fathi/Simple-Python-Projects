# simple prediction game
secret_word = "features"
predict = ""
predict_count = 0
predict_limit = 5
out_of_prediction = False

while predict != secret_word and not out_of_prediction:
    if predict_count < predict_limit :
       predict = input("Enter your prediction : ")
       predict_count += 1
    else:
        out_of_prediction = True
if out_of_prediction :
    print("you lose out of prediction")
else:
    print("You won")
