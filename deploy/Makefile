build-code-uri:
	bash build_code_uri.sh

deploy-workflows-stack: build-code-uri
	cd aichatcore-workflows && \
	sam build && \
	sam deploy

deploy-server-stack: build-code-uri
	cd aichatcore-server && \
	sam build && \
	sam deploy

deploy-client-stack:
	cd aichatcore-client && \
	sam build && \
	sam deploy
