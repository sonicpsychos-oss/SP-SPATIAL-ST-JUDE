.PHONY: build ingest serve clean

build:
	./scripts/build_mockups.py

ingest:
	./scripts/ingest_aec.py

serve:
	python3 -m http.server 8000

clean:
	rm -f dist/*.svg dist/*.json
