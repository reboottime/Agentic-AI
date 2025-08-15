@register_tool(tags=["document_processing", "invoices"])
def extract_invoice_data(action_context: ActionContext, document_text: str) -> dict:
   """
   Extract standardized invoice data from document text. This tool enforces a consistent
   schema for invoice data extraction across all documents.
   
   Args:
       document_text: The text content of the invoice to process
       
   Returns:
       A dictionary containing extracted invoice data in a standardized format
   """
   # Define a fixed schema for invoice data
   invoice_schema = {
       "type": "object",
       "required": ["invoice_number", "date", "amount"],  # These fields must be present
       "properties": {
           "invoice_number": {"type": "string"},
           "date": {"type": "string", "format": "date"},
           "amount": {
               "type": "object",
               "properties": {
                   "value": {"type": "number"},
                   "currency": {"type": "string"}
               },
               "required": ["value", "currency"]
           },
           "vendor": {
               "type": "object",
               "properties": {
                   "name": {"type": "string"},
                   "tax_id": {"type": "string"},
                   "address": {"type": "string"}
               },
               "required": ["name"]
           },
           "line_items": {
               "type": "array",
               "items": {
                   "type": "object",
                   "properties": {
                       "description": {"type": "string"},
                       "quantity": {"type": "number"},
                       "unit_price": {"type": "number"},
                       "total": {"type": "number"}
                   },
                   "required": ["description", "total"]
               }
           }
       }
   }

   # Create a focused prompt that guides the LLM in invoice extraction
   extraction_prompt = f"""
   Extract invoice information from the following document text. 
   Focus on identifying:
   - Invoice number (usually labeled as 'Invoice #', 'Reference', etc.)
   - Date (any dates labeled as 'Invoice Date', 'Issue Date', etc.)
   - Amount (total amount due, including currency)
   - Vendor information (company name, tax ID if present, address)
   - Line items (individual charges and their details)

   Document text:
   {document_text}
   """
   
   # Use our general extraction tool with the specialized schema and prompt
   return prompt_llm_for_json(
       action_context=action_context,
       schema=invoice_schema,
       prompt=extraction_prompt
   )