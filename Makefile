.PHONY: build clean

build:
	./scripts/build_mockups.py

clean:
	rm -f dist/*.svg
