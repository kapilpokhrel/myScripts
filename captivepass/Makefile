PWD:=$(subst /,\\/,$(shell pwd))
all: install

build: requirements.txt
	@if [ -d ".venv" ]; then\
		echo "Using the available virtual environment";\
	else\
		echo "Making a virtual environment"; python -m venv .venv;\
	fi
	( source .venv/bin/activate; pip install -r requirements.txt )

install: build
	@cp ServiceTemplate captivepass.service
	@sed -i "s/{PWD}/$(PWD)/g" captivepass.service
	sudo cp captivepass.service /etc/systemd/system
	sudo systemctl enable captivepass.service
	sudo systemctl start captivepass.service
	sudo systemctl daemon-reload
	@rm captivepass.service
