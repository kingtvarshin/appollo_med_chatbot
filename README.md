# appollo_med_chatbot
 chatbot for hospital

pip install python-dotenv
ref: 
    => venv =>
        => sudo apt install python3-virtualenv
        => virtualenv medbot_venv
        => source medbot_venv/bin/activate
    => download apollo pdf file for raw data sample
    => model => https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
        => llama-2-7b-chat.ggmlv3.q4_0.bin => Quant method:q4_0 :: Bits:4 :: Size:3.79 GB :: Max RAM required:6.29 GB :: Use case:Original quant method, 4-bit.
    => langchain => pip install langchain
    => vector db => chromadb => pip install chromadb
    => document loader => https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf#pypdf-directory
    => text plitter => https://python.langchain.com/docs/modules/data_connection/document_transformers/character_text_splitter
    => embeddings => https://python.langchain.com/docs/integrations/text_embedding/sentence_transformers
        => pip install --upgrade --quiet  sentence_transformers > /dev/null

    <!-- => Simple Python bindings => https://pypi.org/project/llama-cpp-python/
        => pip install llama-cpp-python -->

        pip install ipykernel
        python3 -m ipykernel install --user --name=medbot_venv

        pip install pypdf