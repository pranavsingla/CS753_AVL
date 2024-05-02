# import fairseq
# import hubert_pretraining, hubert
# ckpt_path = "/Users/pranavsingla/CS753_AVL/av_hubert/avhubert/base_lrs3_30h.pt"
# models, cfg, task = fairseq.checkpoint_utils.load_model_ensemble_and_task([ckpt_path])
# model = models[0]
# print(model)

import fairseq
import hubert_pretraining, hubert

# Load the model
model = hubert.AVHubertModel.from_pretrained("/Users/pranavsingla/CS753_AVL/av_hubert/avhubert/base_lrs3_30h.pt")
print(model)
