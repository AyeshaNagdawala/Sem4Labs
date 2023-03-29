echo "Simple Interest"
echo "Enter Principal Amount:"
read principal
echo "Enter Rate of Interest in % per annum:"
read rate_of_interest
echo "Enter Time:"
read time
finalamt=$(((principal * rate_of_interest) * time/100))
echo "Final Amount is $finalamt"
