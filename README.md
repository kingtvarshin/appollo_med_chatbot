# appollo_med_chatbot
 chatbot for hospital


ref: 
    => venv =>
        => sudo apt install python3-virtualenv
        => virtualenv medbot_venv
        => source medbot_venv/bin/activate
    => download apollo pdf file for raw data sample
    => model => https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
        => llama-2-7b-chat.ggmlv3.q4_0.bin => Quant method:q4_0 :: Bits:4 :: Size:3.79 GB :: Max RAM required:6.29 GB :: Use case:Original quant method, 4-bit.
    => Simple Python bindings => https://pypi.org/project/llama-cpp-python/
        => pip install llama-cpp-python