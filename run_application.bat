cd ..
cd venv\scripts
call activate.bat
cd ..
cd ..
cd grafanaautobuilder
python app.py

@REM python stop_messenger.py


@REM pip install -r requirements.txt
@REM python -m document_rag.ingest
@REM python -m sql_rag.query_checker
@REM python -m sql_rag.chart_generator2
@REM python -m sql_rag.schema_creator
@REM python test_panel.py
@REM pip install sqlglot

