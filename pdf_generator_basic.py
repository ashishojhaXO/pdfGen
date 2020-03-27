# import python module
from xhtml2pdf import pisa 
from xhtml2pdf.default import DEFAULT_CSS
from xhtml2pdf import tables
import jinja2
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)

# TEMPLATE_OUTPUT_FILE = [ "invoice_template.html",  "VendorReceipt.pdf" ]
TEMPLATE_OUTPUT_FILE = [ "accelitas_receipt_template.html", "VendorReceipt2.pdf" ]
template = templateEnv.get_template(TEMPLATE_OUTPUT_FILE[0])


body = {
  "data": {
  "order_id": 112241,
  "order_creation_date": "2020-01-23 09:52:51",
  "company_name": "Liberty Hardware",
  "address_1": None,
  "city": None,
  "state": None,
  "zip": None,
  "email": "fusionseven.io@gmail.com",
  "phone": None,
  "paymentmethod_type": "VISA",
  "paymentmethod_last4": "1111",
  "paymentmethod_expirationmonth": "1",
  "paymentmethod_expirationyear": "2021",
  "payment_method": "CC",
  "line_items": [
    {
      "line_item_id": 112241,
      "campaign_line_item_budget": 50.75,
      #"campaign_line_item_budget": "50.75",
      "product": "Facebook"
    },
    {
      "line_item_id": 112242,
      "campaign_line_item_budget": 100.5,
      #"campaign_line_item_budget": "100.5",
      "product": "Facebook"
    }
  ]
}
}
total = sum(i['campaign_line_item_budget'] for i in body['data']['line_items'])
# Define your data
sourceHtml = template.render(json_data=body["data"], total = total)
outputFilename = TEMPLATE_OUTPUT_FILE[1]
print("outputFilename",outputFilename)
html_file = open(str(int(10 * 1001)) + '.html', 'w')
html_file.write(sourceHtml)

# Utility function
def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
    resultFile = open(outputFilename, "w+b")

    pisaStatus = pisa.CreatePDF(
            src=sourceHtml,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    # close output file
    resultFile.close()                 # close output file

    # return True on success and False on errors
    print(pisaStatus.err, type(pisaStatus.err))
    return pisaStatus.err


# Main program
if __name__ == "__main__":
    pisa.showLogging()
    convertHtmlToPdf(sourceHtml, outputFilename)

