import core
import uvicorn

app = core.create_app()
if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=8001,
        workers=2,
        # ssl_version=ssl.PROTOCOL_SSLv23,
        # ssl_keyfile='./core/certs/rootCA-key.pem',
        # ssl_certificate='./core/certs/rootCA.pem',
    )