{
  gROOT->SetBatch(1);
  TList* list = gFile->GetListOfKeys() ;
  TIterator* iter = list->MakeIterator();
  TCanvas *canvas = new TCanvas;

  TKey *key = 0;
  TObject* obj = 0;
  
  while (key = (TKey*)iter->Next()) {
    obj = gFile->Get(key->GetName());
    if (! obj->InheritsFrom(TH1::Class())) continue;
    TH1F* hist = (TH1F*)obj;
    canvas->Clear();
    hist->Draw("HIST");
    canvas->Print(Form("%s.gif",hist->GetName()));
  }


}
