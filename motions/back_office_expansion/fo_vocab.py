#!/usr/bin/env python3
"""Front-office vocabulary for the map pipeline (mode "front_office" in a set's JSON). Applied in place by
bo_titles.configure so every script that imports bo_titles sees the same lanes, topics and functions.
Four lanes mirror the back-office standard: customer operations executives, contact center and service leaders,
workforce management and planning, service technology."""
import re
LANES=[("Customer operations executives", r"\b(chief|coo|cfo|cao|evp|executive vice president|svp|senior vice president)\b|(?<!vice )(?<!vice-)\bpresident\b"),
 ("Workforce management & planning", r"workforce|capacity planning|scheduling|forecasting|real.?time|intraday|command center"),
 ("Service technology", r"technology|ccaas|telephony|\bivr\b|platform|digital|systems|application|automation"),
 ("Contact center & service leaders", r".")]
LANE34=("Workforce management & planning","Service technology")
TOPICS={
 "customer_service":["customer service","customer care","customer support","member service","client service","customer operations","service operations","service center","customer engagement","customer relations","customer success operations","servicing operations","customer contact"],
 "contact_center":["contact center","call center","contact centre","call centre"],
 "experience":["customer experience","client experience","member experience","participant experience","customer contact experience"," cx "],
 "workforce":["workforce","capacity planning","scheduling","forecasting","real time","real-time","intraday","command center","resource planning"],
 "service_tech":["contact center technology","customer service technology","ccaas","telephony","ivr","customer experience technology","digital service","service technology","service platform","customer technology","voice","conversational","chatbot","automation"],
 "service_delivery":["service delivery"],
 "operations":["operations","operating officer","coo"],
 "digital":["digital service","digital operations","digital services","digital customer"],
 "quality":["quality assurance","service quality"],
}
GENERIC={"operations","digital","experience","service_delivery"}
FUNC_RULES=[("Workforce management", r"workforce|capacity planning|scheduling|forecasting|real.?time|intraday|command center|resource planning"),
 ("Service technology", r"technology|ccaas|telephony|\bivr\b|platform|digital|systems|application|automation|conversational|chatbot"),
 ("Contact center operations", r"contact cent|call cent|customer contact"),
 ("Customer experience", r"customer experience|client experience|member experience|\bcx\b"),
 ("Customer service operations", r".")]
KEEP_TECH=r"contact center technology|customer service technology|customer experience technology|service technology|ccaas|telephony|\bivr\b|digital service|customer technology|service platform|conversational|contact center (platform|systems|solutions)|customer (care|service|experience) (platform|systems|solutions)"

# titles that carry a front-office word but are not the front office (design, HR, treasury, product, tech infrastructure)
EXCLUDE=r"experience design|user experience|\bux\b|design director|content|communications|identity|contingent workforce|people experience|teammate experience|organizational health|hosting|treasury|lockbox|equity compensation|digital assets|stock plan|tax exempt|product leader|carrier management|branch manager|corporate services|finance executive|institutional services|commercial card|cra director|asset lifecycle|workforce intelligence|talent|customer insights|client insights|messaging experience|duals experience|claims experience|health support|children medical|complex care|alternatives|forecasting strategist|asset liability|utilization management|product management"
