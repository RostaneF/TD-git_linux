import requests
import exo3

def main():
	df = exo3.get_manors_info("dby")
	print(df["geld"].sum())
	print(df["totalploughs"].sum())

if __name__ == "__main__":
	main()
