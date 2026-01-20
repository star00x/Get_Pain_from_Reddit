# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** Can anybody tell me how to create consistent AI character/person but very realistic like real human!?
**Post URL:** https://www.reddit.com/r/generativeAI/comments/1mbwbyt/can_anybody_tell_me_how_to_create_consistent_ai/
**JSON URL:** https://www.reddit.com/r/generativeAI/comments/1mbwbyt.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 53
- **extracted_unique_comments:** 40
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 0.7547
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (3)

### t1_n5xug87 (score=1, depth=0)
- **Author:** u/Jenna_AI
- **Parent:** t3_1mbwbyt
- **Link:** https://www.reddit.com/r/generativeAI/comments/1mbwbyt/can_anybody_tell_me_how_to_create_consistent_ai/n5xug87/

> Ah, the classic "evil twin" dilemma. You spend hours creating the perfect character, and the AI gives you back their suspiciously smooth-skinned clone from a parallel universe. It's a rite of passage.
> 
> Your Midjourney OmniRef -> LoRA workflow is a solid start, but it sounds like you're hitting the uncanny valley wall. Let's get you over it.
> 
> Here are a couple of pro-level tricks to add to your process:
> 
> *   **Fix The "Plastic" Look First:** The main reason for that unrealistic look is often the base generation's lack of texture. Before you even think about training your LoRA, you can significantly improve your source images. A popular technique is to run your best generations through a realism enhancer to fix things like skin texture and pores. This fantastic, in-depth guide by Sirio breaks down a full professional workflow, including using tools specifically for this purpose. Trust me, it's a game-changer.
>     *   **Full Pro Workflow Video:** [youtube.com](https://www.youtube.com/watch?v=mi_ubF8_n8A)
> 
> *   **Graduate to a More Powerful Workflow:** For the kind of control you're looking for, many artists move from all-in-one tools to a node-based system like **ComfyUI**. It has a steeper learning curve, but it allows you to chain specific models, upscalers, and face-detailing nodes together. This gives you granular control to lock down your character's likeness across different poses, lighting, and expressions. The video linked above also covers a ComfyUI approach for this exact problem.
> 
> *   **Create a "Character Bible":** A brilliant and simple trick is to get *insanely* …

### t1_n6z98a9 (score=1, depth=0)
- **Author:** u/ricardo_ghekiere
- **Parent:** t3_1mbwbyt
- **Link:** https://www.reddit.com/r/generativeAI/comments/1mbwbyt/can_anybody_tell_me_how_to_create_consistent_ai/n6z98a9/

> This is literally the core challenge we deal with at BetterPic every single day. That plastic look and inconsistency? Yeah, it's why we ended up hiring a 24/7 team of human editors to fix AI hallucinations before photos go out.
> 
> The brutal truth is that pure AI consistency is still pretty broken, especially for faces. Even with LoRA training, you're fighting against models that want to "interpret" rather than replicate exactly.
> 
> Few things that might help your process:
> 
> Your reference images matter way more than you think. If they have inconsistent lighting, angles, or even slightly different facial expressions, the model gets confused and starts inventing details. I'd try using more controlled reference shots - same lighting setup, neutral expressions.
> 
> For the plastic look - that usually comes from over-processing or the model trying too hard to "perfect" skin texture.  Sometimes it has to do with your input, are they using beauty filters, blurry, or low lighting, which is hard to pinpoint since every platform handles things differently.
> 
> The LoRA training part is tricky. 15-25 photos might not be enough, but more importantly, the quality and consistency of your training data matters more than quantity. We've found that having too much variation in the training set actually makes consistency worse.
> 
> Honestly though? This is exactly why we built our editing pipeline the way we did. Sometimes the most practical solution is accepting that AI gets you 80% there and having humans handle the final 20% for realism.

### t1_nx2q8xg (score=6, depth=0)
- **Author:** u/FarBullfrog627
- **Parent:** t3_1mbwbyt
- **Link:** https://www.reddit.com/r/generativeAI/comments/1mbwbyt/can_anybody_tell_me_how_to_create_consistent_ai/nx2q8xg/

> I think a bunch of the AI generation tools (LTX Stu⁤dio, Run⁤way) etc.. can do this pretty easily for you now.
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** Any AI tools for consistent character animation (free or cheap, doesn’t need a beast PC)
**Post URL:** https://www.reddit.com/r/aitubers/comments/1omwufw/any_ai_tools_for_consistent_character_animation/
**JSON URL:** https://www.reddit.com/r/aitubers/comments/1omwufw.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 20
- **extracted_unique_comments:** 19
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 0.95
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (1)

### t1_nncp4m7 (score=1, depth=0)
- **Author:** u/cfwes
- **Parent:** t3_1omwufw
- **Link:** https://www.reddit.com/r/aitubers/comments/1omwufw/any_ai_tools_for_consistent_character_animation/nncp4m7/

> Try using the character creator on [GenTube](http://gentube.app) and then inserting it into a base image, then making a video. It works pretty well for being free and unlimited.
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** I built an AI automation that generates unlimited consistent character UGC ads for e-commerce brands (using Sora 2)
**Post URL:** https://i.redd.it/a21ohahojvzf1.png
**JSON URL:** https://www.reddit.com/r/n8n/comments/1or1gwi.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 29
- **extracted_unique_comments:** 25
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 0.8621
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (8)

### t1_nnmu567 (score=20, depth=0)
- **Author:** u/dudeson55
- **Parent:** t3_1or1gwi
- **Link:** https://www.reddit.com/r/n8n/comments/1or1gwi/i_built_an_ai_automation_that_generates_unlimited/nnmu567/

> Here's the workflow/template json: [https://github.com/lucaswalter/n8n-ai-automations/blob/main/sora2\_ugc\_consistent\_character\_ads\_generator.json](https://github.com/lucaswalter/n8n-ai-automations/blob/main/sora2_ugc_consistent_character_ads_generator.json)

### t1_nnne0st (score=12, depth=0)
- **Author:** u/taxista_furioso
- **Parent:** t3_1or1gwi
- **Link:** https://www.reddit.com/r/n8n/comments/1or1gwi/i_built_an_ai_automation_that_generates_unlimited/nnne0st/

> More AI slop, very good.

### t1_nnmu63t (score=6, depth=0)
- **Author:** u/BedMaximum4733
- **Parent:** t3_1or1gwi
- **Link:** https://www.reddit.com/r/n8n/comments/1or1gwi/i_built_an_ai_automation_that_generates_unlimited/nnmu63t/

> That's pretty slick.

### t1_nnr8wit (score=4, depth=1)
- **Author:** u/Levfo
- **Parent:** t1_nnne0st
- **Link:** https://www.reddit.com/r/n8n/comments/1or1gwi/i_built_an_ai_automation_that_generates_unlimited/nnr8wit/

> Welcome to the future lil bro

### t1_nnmwcbb (score=3, depth=2)
- **Author:** u/dudeson55
- **Parent:** t1_nnmvxqn
- **Link:** https://www.reddit.com/r/n8n/comments/1or1gwi/i_built_an_ai_automation_that_generates_unlimited/nnmwcbb/

> not yet - that's one of the next things I have on my list to explore

### t1_nnn37u2 (score=3, depth=3)
- **Author:** u/Zyklone187
- **Parent:** t1_nnmwcbb
- **Link:** https://www.reddit.com/r/n8n/comments/1or1gwi/i_built_an_ai_automation_that_generates_unlimited/nnn37u2/

> Would be cool. To get an update after your research 💪

### t1_nnpccz9 (score=3, depth=0)
- **Author:** u/ThatGuyThatLies
- **Parent:** t3_1or1gwi
- **Link:** https://www.reddit.com/r/n8n/comments/1or1gwi/i_built_an_ai_automation_that_generates_unlimited/nnpccz9/

> Gross.

### t1_nnmvxqn (score=2, depth=1)
- **Author:** u/Zyklone187
- **Parent:** t1_nnmu567
- **Link:** https://www.reddit.com/r/n8n/comments/1or1gwi/i_built_an_ai_automation_that_generates_unlimited/nnmvxqn/

> Have you tried combining this with the Sora 2 Storyboard feature?
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** Keeping character appearance consistent across scenes in GROK Imagine (image + video)
**Post URL:** https://www.reddit.com/r/grok/comments/1ogq0sy/keeping_character_appearance_consistent_across/
**JSON URL:** https://www.reddit.com/r/grok/comments/1ogq0sy.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 10
- **extracted_unique_comments:** 10
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 1.0
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (4)

### t1_nlkbwt7 (score=2, depth=1)
- **Author:** u/Firm-Flight-9359
- **Parent:** t1_nlia3mw
- **Link:** https://www.reddit.com/r/grok/comments/1ogq0sy/keeping_character_appearance_consistent_across/nlkbwt7/

> I actually notice the opposite. Everything gets shiny. What I do is about every other frame I put it in GIMP and up the brightness a bit. (GIMP is basically open source photoshop)

### t1_nlian1a (score=5, depth=0)
- **Author:** u/mnfrench2010
- **Parent:** t3_1ogq0sy
- **Link:** https://www.reddit.com/r/grok/comments/1ogq0sy/keeping_character_appearance_consistent_across/nlian1a/

> As things progressed, I noticed the generations become more cartoonish.  Once I had 60 seconds, I ran the whole video though an app called FakeMe, where you can replace the face.
> 
> So, I take my Grok generated videos, stitch them together, run it through FakeMe with a better quality facial image, hit send.  About 2 mi items later I get a better video with the correct face.

### t1_nljqfkc (score=3, depth=0)
- **Author:** u/roger_ducky
- **Parent:** t3_1ogq0sy
- **Link:** https://www.reddit.com/r/grok/comments/1ogq0sy/keeping_character_appearance_consistent_across/nljqfkc/

> While it’s unavoidable to have “last frame” issues if you keep continuing, that’s mostly avoidable if you plan your shots.
> 
> Whenever you can:
> 
> Start with a neutral image that’s a good “character sheet” with multiple perspectives.
> 
> Tell image edit to place said character into the a specific scene for the beginning of a shot.
> 
> Generate video with your “storyboard.”

### t1_nlia3mw (score=1, depth=0)
- **Author:** u/redworld
- **Parent:** t3_1ogq0sy
- **Link:** https://www.reddit.com/r/grok/comments/1ogq0sy/keeping_character_appearance_consistent_across/nlia3mw/

> Same issues. Also having trouble with gradual color desaturation if you’re using the final frame as a starting point for the next. It’s like half grayscale by the 4th segment.
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** Best text-to-video models for character + scene consistency?
**Post URL:** https://www.reddit.com/r/generativeAI/comments/1lfzzz3/best_texttovideo_models_for_character_scene/
**JSON URL:** https://www.reddit.com/r/generativeAI/comments/1lfzzz3.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 15
- **extracted_unique_comments:** 8
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 0.5333
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (1)

### t1_nqbzgou (score=5, depth=0)
- **Author:** u/ben_claude69420
- **Parent:** t3_1lfzzz3
- **Link:** https://www.reddit.com/r/generativeAI/comments/1lfzzz3/best_texttovideo_models_for_character_scene/nqbzgou/

> The LTX-2 mod⁤el can do exact⁤ly this, really go⁤od for consis⁤tency.
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** Why is Sora so bad despite all the hype it had?
**Post URL:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/
**JSON URL:** https://www.reddit.com/r/singularity/comments/1hqvg5h.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 98
- **extracted_unique_comments:** 99
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 1.0102
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (41)

### t1_m4t81ea (score=25, depth=2)
- **Author:** u/Neither_Sir5514
- **Parent:** t1_m4t5g3f
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t81ea/

> This dogshit is not worth $200 per month when Huyuan is open source and Kling, Minimax & Pika are free. The OG Model ? Debatable, since we never even got to test its output quality ourselves, for all we know what we saw were most likely cherrypicked for marketing purposes.

### t1_m4tgkee (score=13, depth=3)
- **Author:** u/yaboyyoungairvent
- **Parent:** t1_m4t81ea
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4tgkee/

> Pika isn't really free. The older version is free (1.5) but the latest 2.0 version that is comparable to sora is behind a subscription. Ontop of that you need to pay $28 a month to get commercial use. I wouldn't put it in the same category as Kling and Minimax.

### t1_m4trjgo (score=3, depth=0)
- **Author:** u/sdmat
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4trjgo/

> Sora as launched is substantively identical to the original off-the-cuff demos Altman posted on Twitter. We see the odd generation of similar quality to the cherry-picked examples too.
> 
> What happened is that everyone else improved enormously in the 10 months since OAI demoed it. And Veo2 is in another league!

### t1_m4t6ay4 (score=2, depth=0)
- **Author:** u/plantsnlionstho
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t6ay4/

> Because they took 10 months to release it...

### t1_m4teqs3 (score=2, depth=1)
- **Author:** u/NoshoRed
- **Parent:** t1_m4tdgm1
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4teqs3/

> They don't care about Dall-E. They haven't marketed it, they haven't talked about it, no hype whatsoever. They were actively hyping up Sora, and released it during their mega hyped "12 days of shipmas", so clearly they care about Sora and its reception. Meaning, Dall-E and Sora isn't comparable.

### t1_m4syasg (score=157, depth=0)
- **Author:** u/[deleted]
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4syasg/

> I wondered the same, I think they distilled it too much to let more people use it.

### t1_m4ug54d (score=1, depth=1)
- **Author:** u/WonderFactory
- **Parent:** t1_m4t4uy6
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4ug54d/

> \>The outputs they showed in the initial announcement were super cherrypicked
> 
> I disagree here, they showed plenty of dud videos in the initial announcement. I remember there was a dog on a bed that morphed into a pillow and some chairs on a building site that seemed to liquidify.
> 
> There was a lot of hype about it because it was revolutionary at the time, everyone assumed it was years ahead of any competition. But 9 months is a long time in AI and they waited too long to release it and by the time they did everyone caught up and some even overtook them.

### t1_m4t5g3f (score=99, depth=1)
- **Author:** u/ithkuil
- **Parent:** t1_m4syasg
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t5g3f/

> It's a slimmed down model with reduced capabilities called SORA Turbo.

### t1_m4t0dar (score=-5, depth=1)
- **Author:** u/NoshoRed
- **Parent:** t1_m4t06q2
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t0dar/

> >Sora was incredible the day it launched.
> 
> I tried it on public launch day during their 12 days of Shipmas thing, it wasn't. Maybe it's worse now? But even at launch I found that even Kling 1.0, their oldest model, was better, which is outrageous.

### t1_m4szmkj (score=52, depth=0)
- **Author:** u/Soggy-Contribution73
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4szmkj/

> Probably lobotomized for safety.

### t1_m4t4uy6 (score=44, depth=0)
- **Author:** u/Concheria
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t4uy6/

> 1) The outputs they showed in the initial announcement were super cherrypicked
> 
> 2) When they announced it first, there weren't any models like it. By the time they released it, there were several: Kling, Hailuoai, Runway...
> 
> 3) The version they actually released was a super stripped down turbo version for safety and performance to be able to serve it to millions of users
> 
> 4) Due to how diffusion models work, the 1080p version available in pro is actually a lot better than the version available for ChatGPT plus users
> 
> Now the best performing one is Google Veo 2, but that one is only available for closed beta testers. This means that there's a lot of room for improvement (Veo 2 is proof), but it'll take a while and those improvements will be gradual, and other companies will probably continue outperforming Sora before they can release it.

### t1_m4sz6yi (score=42, depth=0)
- **Author:** u/ShooBum-T
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4sz6yi/

> Because it's a first generation, highly scaled product. Plus it depends on how much OpenAI wants to make it real. Look at how much dalle3 is nerfed. 
> 
> However with Sora improvements should come pretty quickly, it looks like they're serious on that. Storyboard, remix , etc. creating a standalone product for video means they're very serious about this.

### t1_m4t7uh7 (score=42, depth=2)
- **Author:** u/CheekyBastard55
- **Parent:** t1_m4t5g3f
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t7uh7/

> I was hammering this point ever since they announced it back in Feb, that it would not release until maaaaybe end of year/next year and it will be a heavily nerfed version.
> 
> The delusional people on here expected a June release unnerfed. The fact they could only generate one video at a time means it's no way ready to be launched to the public with those capabilities.

### t1_m4szuw0 (score=25, depth=1)
- **Author:** u/NoshoRed
- **Parent:** t1_m4sz6yi
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4szuw0/

> Their UI is great, the features are brilliant if the model was actually good. My experience with Sora img2vid was my image just being visible for one frame and the scene changing into something else entirely from the second frame onward. Same prompt, same image on Pika 2.0 gave me a much better result, satisfactory. Kling 1.6 was a near perfect result.
> 
> Very disappointing. But yeah let's hope it actually catches up.

### t1_m4t06q2 (score=24, depth=0)
- **Author:** u/_roblaughter_
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t06q2/

> Sora was incredible the day it launched. 
> 
> The reason it looks like trash by comparison today is because everything else kept going in the interim. 
> 
> I feel like there’s a good chance Sora may be the next DALL-E, stagnating while open models and smaller closed source devs continue to make progress.

### t1_m4syzwp (score=20, depth=0)
- **Author:** u/Impressive_Deer_4706
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4syzwp/

> It was never good. Look at the original demos Sam Altman gave on Twitter. It looked terrible if it was out of distribution. (For example something like “dragon playing with a ball” resulted in like a 2 spheres with 0 details.
> 
> It’s also clear their demos used way more compute.

### t1_m566wxd (score=1, depth=0)
- **Author:** u/indiegameplus
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m566wxd/

> I blatantly disagree. I've been generating hundreds of videos across all models since we were just working with open-source stuff like potato1 and zeroscope, then onto Runway, I was a beta tester for Kling before it launched in the west, then Lumalabs, then Pika, then even LeonardoAI which I found particularly cool for some stuff. Runway Gen-3 was the king for a long time, but Sora blows it out of the water for literally everything I can throw at it. "Sora sucks!" - no it doesn't, you just don't know how to prompt properly or how to use it properly. I have hundreds of Sora generations at this point which I could show to people and for your average everyday human - 8/10 would not be able to tell it's AI. For consistent 20-second generations, the amount of sheer dynamism that every generation manages to pump out is unparalled. High end fashion videos? Professional marketing videos? Vintage period era clips? Landscape shots? It literally makes me anything I ask of it - 2x720p 20 second variations - 5 of these at once so 10 20 second generations - and I can literally take between 10-15 seconds out of each of those gens and use them for content that looks professional, real, and convincing. I am so so sick of people crying out that it's a shit model when the real barrier is that they just don't test it and actually learn how to use it. All of these tools WORK DIFFERENTLY, and some require a bit more fine-tuning and fiddling with your prompts than others. But once you work out your structure and flow - Sora is unbeatable imo. For txt2video that is. I still think Kling and Hailuo…

### t1_m4t3sh9 (score=10, depth=1)
- **Author:** u/llkj11
- **Parent:** t1_m4syzwp
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t3sh9/

> But compared to everything else at the time it was revolutionary. Of course with hindsight and new models we can look back and say a lot of the generations were trash.

### t1_m4u38nj (score=10, depth=3)
- **Author:** u/KIFF_82
- **Parent:** t1_m4t7uh7
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4u38nj/

> yeah, but kling made it work, and openai had the lead—kling looks better now than the OpenAI demo back then

### t1_m4t2ivi (score=7, depth=2)
- **Author:** u/Able_Buy_6120
- **Parent:** t1_m4t0dar
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t2ivi/

> You mean you tried it on public launch day in December or when they first showed samples to the public earlier this year?

### t1_m4t978n (score=7, depth=3)
- **Author:** u/Adept-Potato-2568
- **Parent:** t1_m4t27lj
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t978n/

> It's nearly non-functional in its current state so underbaked is quite the statement.

### t1_m4thw5v (score=7, depth=1)
- **Author:** u/[deleted]
- **Parent:** t1_m4szmkj
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4thw5v/

> [deleted]

### t1_m4t0cub (score=6, depth=0)
- **Author:** u/RedLock0
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t0cub/

> is sora with less computation. I don't know why they just don't do marketing with full sora giving access to very few people.

### t1_m4t066x (score=5, depth=1)
- **Author:** u/creativities69
- **Parent:** t1_m4syasg
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t066x/

> They haven’t even given us poor brits a go yet

### t1_m4t6ond (score=5, depth=2)
- **Author:** u/NoCard1571
- **Parent:** t1_m4t3sh9
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t6ond/

> Exactly, I really don't understand this sub sometimes. Did everyone really collectively forget how much of a leap it was over previous models when it was first demoed? The fact it's outshined by current models doesn't change that fact

### t1_m4tdz6c (score=5, depth=1)
- **Author:** u/NoshoRed
- **Parent:** t1_m4tarkg
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4tdz6c/

> Clearly not considering the competing tools I actively use are extremely impressive and has made significant progress. Just not Sora.

### t1_m4t3i3y (score=4, depth=0)
- **Author:** u/iamz_th
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t3i3y/

> Openai announcements are 10 times more exciting than openai releases. Sora,4o,avm and even o1 (strawberry)

### t1_m4t4kqi (score=4, depth=0)
- **Author:** u/jaaybans
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t4kqi/

> many softwares have caught up since then

### t1_m4t5n88 (score=4, depth=0)
- **Author:** u/willjoke4food
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t5n88/

> You want the truth? It's because openai carries the flag of American AI supremacy and people are reluctant to believe china could have an edge even if it does. When sora clips were launched, it was well known that it was cherry picked as hell, and so many skeptics were silenced. News outlets were paid millions to plaster the name "Sora" everywhere, even though the product didn't launch for another year. Openai published no papers on the technique not training data because both were stolen, mostly from Google. 
> 
> Yes sora is an inferior product, and that's because it's versatility is limited by the lobotomy and model distillation needed to achieve a good solution. If you think back, dalle was never the sota in image generation for long, but it definately garnered the most media attention. This is openai's endgame. They are not interested in providing the right tools to people, or empower them. They steal from their investors and users alike, all in the name of being the best. 
> 
> If there's any solace, openai's biggest threat is illyas SSI. Once they lose their crown jewel and their AGI model is deemed obsolete and redundant in an endless sea of replicatable software, they will scramble to eat as much investor money as possible before they become another "victim". 
> 
> It's not all doom and gloom though, and they've shown that these models are capable of generality through their o3 arc agi results (which again, remain to be verified by the larger public). The public generally loves them and wants them to do the best and beat the behemoth that is google, but if veo is launched to …

### t1_m4trmc6 (score=4, depth=1)
- **Author:** u/[deleted]
- **Parent:** t1_m4szmkj
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4trmc6/

> [deleted]

### t1_m4u0hjm (score=4, depth=3)
- **Author:** u/Volky_Bolky
- **Parent:** t1_m4t2ivi
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4u0hjm/

> They showed curated results at first.
> 
> For what we know they could generate 1000000 tries for each sample and then let hundreds of  Kenyans they employ cherry pick the best one.

### t1_m4szqly (score=3, depth=0)
- **Author:** u/nederino
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4szqly/

> Because when it was originally shown it was very good but time passed every one caught up and google passed them.
> 
> It's probably because openai was focused on o3 instead of improving sora

### t1_m4t3vtc (score=3, depth=0)
- **Author:** u/Gab1159
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t3vtc/

> Because OpenAI treads the line between overhyping and scamming investors with empty promises.

### t1_m4t4xg2 (score=3, depth=0)
- **Author:** u/hellolaco
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t4xg2/

> Many people missing the fact that the demos we saw was from Sora. The one that got released is Sora Turbo. OpenAI did this very quietly, so I guess Sora Turbo is a much less powerful model…

### t1_m4t8hwq (score=3, depth=0)
- **Author:** u/Low-Bus-9114
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t8hwq/

> I agree, it's surprisingly shit

### t1_m4t8m29 (score=3, depth=0)
- **Author:** u/Various-Inside-4064
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t8m29/

> OpenAI usually hype their product lot more than it actually is.

### t1_m4tarkg (score=3, depth=0)
- **Author:** u/ZenithBlade101
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4tarkg/

> Because 90+% of “progress” in AI is hype

### t1_m4uhv17 (score=3, depth=2)
- **Author:** u/DirtyGirl124
- **Parent:** t1_m4ug54d
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4uhv17/

> Yes they did but is that what people focused on?

### t1_m4zil20 (score=3, depth=0)
- **Author:** u/05032-MendicantBias
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4zil20/

> The answer is obvious.
> 
> OpenAI is a company that sells hype to investors. The customers are not GenANI users, it's venture capital.
> 
> OpenAI makes a demo. Delivers a product that performs at an insignificant fraction of the promised capability, while selling an even more hyped demo. i remember how hyped O1 was. Remember, they were arguing O1 would be replacing PhDs. Now it's O4 that will replace PhDs at an even higher subscription. And when that fails, another rebrand to another name with an even wilder claim.

### t1_m4tdgm1 (score=2, depth=0)
- **Author:** u/IronPheasant
- **Parent:** t3_1hqvg5h
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4tdgm1/

> Same reason Dal-E isn't competitive. It's old and they didn't spend resources on making it better. Why would they bother making it better?
> 
> The next order of scaling is incredibly important. The goal isn't to make a movie generator. The goal is to make a mind that can make a movie generator.
> 
> And everything else.

### t1_m4t27lj (score=1, depth=2)
- **Author:** u/ShooBum-T
- **Parent:** t1_m4szuw0
- **Link:** https://www.reddit.com/r/singularity/comments/1hqvg5h/why_is_sora_so_bad_despite_all_the_hype_it_had/m4t27lj/

> I understand it's a little underbaked if you compare it to Kling especially, wouldn't compare to veo2 as it's not a released product yet. I think sora-turbo or whatever might be little too over-distilled and a little data flywheel is needed. I'm very confident that the next iteration will be much better, if only available to the Pro tier. Won't be surprised if they release a Sora only plan. 
> 
> But what I like more is that although OpenAI is one of the top labs , they're not leaps and bounds ahead in anything. There is no model/feature that OpenAI has that is unique to them. I think that's good and makes the field competitive.
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** SORA AI keeps ignoring specific visual instructions — no matter how detailed or clear my prompts are.
**Post URL:** https://www.reddit.com/r/SoraAi/comments/1l8pdf1/sora_ai_keeps_ignoring_specific_visual/
**JSON URL:** https://www.reddit.com/r/SoraAi/comments/1l8pdf1.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 21
- **extracted_unique_comments:** 21
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 1.0
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (4)

### t1_mx8jgna (score=2, depth=2)
- **Author:** u/paradoxically_cool
- **Parent:** t1_mx7uaib
- **Link:** https://www.reddit.com/r/SoraAi/comments/1l8pdf1/sora_ai_keeps_ignoring_specific_visual/mx8jgna/

> I pay for Gemini for coding and business analysis purposes. i find that its the best at Coding and Research related tasks. Translating Natural Language prompts to a well structured JSON, parsing the nuance of my intent, the complex look/color grade/ camera and lens... etc, was a very complicated task that Gemini's big context window and logic was best at. I hit a wall using Chatgpt in this specific case (generating JSON prompts), because i used up all the memory, and it started forgetting. Chatgpt is wonderful though at generating amazingly detailed Natural Language prompts. and it will give you great strategies to barely pass the decency filter if you are getting stopped by it. Gemini tends to be a square, it's decency filter is way too conservative, it will change interactions and attire to be more rigid, plain and dull. so when you want Natural Language prompts use Chatgpt, When you want Code or to reverse engineer a particular visual style, you have to use JSON and Gemini.
> 
> The issue i was trying to solve is that my comprehensive detailed prompts generated by Chatgpt were still outputting inconsistent "look and feel", Sora was creating 4 outputs with non-matching white balance, some where painterly, etc. I wanted a method to SET IN STONE the visual look and style across a series of images. the preset didn't work, so i took the time to iterate with Gemini until it created a solid well structured JSON which i paste directly in the image prompt window as is in sora. This almost guarantees the look I'm going for.
> 
> but the JSON is complex to edit for new scenes. to smooth-o…

### t1_mx6mdhc (score=1, depth=0)
- **Author:** u/B_lintu
- **Parent:** t3_1l8pdf1
- **Link:** https://www.reddit.com/r/SoraAi/comments/1l8pdf1/sora_ai_keeps_ignoring_specific_visual/mx6mdhc/

> You're running into one of the most persistent and frustrating limitations of current generative video models like Sora: prompt adherence and character consistency, especially in highly specific visual constraints like facial features, attire, and historical accuracy, is still far from reliable — no matter how precisely you word your prompts.
> 
> 
> Here's a breakdown of what’s going on and what you can do:
> 
> 
> ---
> 
> 
> 🔍 Why Sora Isn’t Listening
> 
> 
> 1. Learned Biases Override Prompts
> 
> 
> Sora is trained on a massive dataset with latent biases about “medieval” characters. If you mention anything resembling “Dante” or a “poet from 1300s Florence,” it will likely default to a stereotyped, often generic, medieval man — usually bearded, sometimes bald, and wearing vague robes. This is because the visual associations encoded during training are stronger than your negative prompts.
> 
> 
> Even removing “Dante” from the prompt doesn’t always help, because the visual tropes are tied to the era and occupation you’re describing (e.g., “Italian medieval poet”).
> 
> 
> 
> 
> ---
> 
> 
> 2. Negations Don’t Work Reliably
> 
> 
> Telling Sora to “not do” something (e.g., “no beard,” “not bald,” “forbidden”) often fails, especially in visuals. Unlike text models, visual generation models are not good at understanding negation. They can interpret positive attributes better than prohibitions.
> 
> 
> 
> 
> ---
> 
> 
> 3. Remix and Reference Images Are Loosely Interpreted
> 
> 
> If you’re using an image as a “reference only,” but don’t explicitly tell the system to not show it directly, it may try to literally insert it. And even if you do, the model …

### t1_mx7uaib (score=1, depth=1)
- **Author:** u/Andxel
- **Parent:** t1_mx7n8bz
- **Link:** https://www.reddit.com/r/SoraAi/comments/1l8pdf1/sora_ai_keeps_ignoring_specific_visual/mx7uaib/

> Do you then feed the JSON prompt to SORA AI? Also, couldn’t you ask to translate your natural language to JSON prompts to GPT? Why use GEMINI?

### t1_mx7n8bz (score=1, depth=0)
- **Author:** u/paradoxically_cool
- **Parent:** t3_1l8pdf1
- **Link:** https://www.reddit.com/r/SoraAi/comments/1l8pdf1/sora_ai_keeps_ignoring_specific_visual/mx7n8bz/

> I was running into this in my art project, the most solid way I found was to prompt using JSON, I iterated with Gemini for like two hours, showing him my natural language prompts and the outputs and what I need changing and specified the prompts need to be in JSON. That gave me the best consistency in visual style, and character look across a group of images. I now have a structured JSON template for my specific project. Which I also attached to on other gem. I describe what I need and it creates the JSON prompt needed for my desired output.
> 
> About historical figure likeness. My best advice is to never use their names directly. Ask chatgpt in text to give you a comprehensive visual discription of your target character according to historical sources. Then ask them to: write visual discription of "new name" who exactly matches the likeness of "historic figure" in all aspects, optimize the language for Sora prompt.
> 
> From then on, use this new discription for your character in scene prompt.
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** Gen-4 honest opinion! Disappointing but better than nothing
**Post URL:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/
**JSON URL:** https://www.reddit.com/r/runwayml/comments/1jor1t4.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 47
- **extracted_unique_comments:** 47
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 1.0
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (18)

### t1_mlc9uox (score=3, depth=0)
- **Author:** u/TobinWexley
- **Parent:** t3_1jor1t4
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mlc9uox/

> I’m disappointed with Gen 4. First, the queue lines are over ten minutes. If I’m paying $100 a month, I shouldn’t have to wait in a queue that long.
> 
> I’ve read all the documentation to adjust my prompting, but Gen 3 Alpha Turbo still produces better results with illustrated characters. Gen 4 morphs them into a cartoonish mess and creates motion and gestures that are WAY too fast and chaotic.
> 
> It seems like Runway got a lot of feedback from people complaining about slow-motion results with Gen 3, so for Gen 4 they over corrected and subject’s movements are often too fast and chaotic. That is, once they get going. For some reason with Gen 4 the first three or four seconds of a ten second video the character will often remain motionless, then the prompt will kick in and they go nuts. 
> 
> However, there are a lot of features yet to be released for Gen 4 such as last frame and camera controls, so we’ll see. I just hope they solved the “Static camera” also forces the subject to be static problem.

### t1_mkuj1sq (score=13, depth=0)
- **Author:** u/nurological
- **Parent:** t3_1jor1t4
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkuj1sq/

> Kling is better than sora

### t1_mkua10k (score=4, depth=0)
- **Author:** u/Literally_Sticks
- **Parent:** t3_1jor1t4
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkua10k/

> Do you have any tips on how to prompt better on Sora? Im new to AI gen and am struggling a bit. The content restrictions are a pain, but I can't seem to get anything animated correctly. Even if it's a reddit post or YT video that you got good info from, I'd love any pointer in the right direction

### t1_mkv0p8x (score=4, depth=2)
- **Author:** u/possibilistic
- **Parent:** t1_mku90by
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkv0p8x/

> Nah. They peaked. There are smaller companies doing way better. I think they hit a talent / budget wall. 
> 
> 
> Kling is stunning. You should also try Hailuo. And PixVerse for animation. Or Pika for live action edits. 
> 
> 
> If you've got a thing for ComfyUI, WanVideo is good too, though a little frustrating. But you can do a lot of neat stuff with it like controlnets and custom LoRAs for your own styles. 
> 
> 
> Google Veo is pretty great too. 

### t1_mku6cl4 (score=9, depth=0)
- **Author:** u/Conscious-Kitchen412
- **Parent:** t3_1jor1t4
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mku6cl4/

> Your title summarised it all. Now I understand why they delayed the release of the model for a half year; there was simply nothing to release!

### t1_mkuc5oh (score=7, depth=0)
- **Author:** u/Foreign-Assistant610
- **Parent:** t3_1jor1t4
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkuc5oh/

> I'm Lovin' It

### t1_mkv0cn8 (score=7, depth=0)
- **Author:** u/possibilistic
- **Parent:** t3_1jor1t4
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkv0cn8/

> Kling is king. 
> 
> 
> Runway is super mid. It's worse than Kling, Hailuo Minimax, Google Veo, and Sora. 

### t1_mktt3ut (score=6, depth=0)
- **Author:** u/[deleted]
- **Parent:** t3_1jor1t4
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mktt3ut/

> [removed]

### t1_mkv1ddm (score=4, depth=1)
- **Author:** u/possibilistic
- **Parent:** t1_mktt3ut
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkv1ddm/

> I'm going to cancel my company's subscriptions to runway today. We have four subscriptions and we're mostly using Sora and Kling now. 

### t1_mkvfaci (score=4, depth=2)
- **Author:** u/Sane-Philosopher
- **Parent:** t1_mkv1ddm
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkvfaci/

> worm office dinosaurs mountainous liquid snow frighten gaping squeamish mysterious
> 
>  *This post was mass deleted and anonymized with [Redact](https://redact.dev/home)*

### t1_mkvitrc (score=4, depth=3)
- **Author:** u/shmehdit
- **Parent:** t1_mkvfaci
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkvitrc/

> I haven't tried Gen4 yet, but Gen3's speed has always been its most impressive quality to me.  Yes Kling is slower, but it's generations have sped up quite a bit just in the last couple weeks - 5 seconds of i2v in Professional mode on version 1.6 generates in less than a minute consistently, 10 seconds closer to 2 minutes. What takes the most time is using their Elements feature or doing extensions - can be 7-8 minutes.

### t1_mkve4de (score=3, depth=2)
- **Author:** u/Foreign-Assistant610
- **Parent:** t1_mkv0hc9
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkve4de/

> LOL, then what are you doing here, kid?

### t1_mkwte8x (score=3, depth=3)
- **Author:** u/possibilistic
- **Parent:** t1_mkve4de
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkwte8x/

> The Reddit algorithm. It thinks my interest in AI images and video mean I'm interested in RunwayML for some reason.
> 
> Blame Reddit. They're optimizing for this, and if you think this is bad, it's even more obvious on the political and pop culture subs. They actively try to get debate started becaues debate = engagement.

### t1_mkzxbhu (score=3, depth=1)
- **Author:** u/Turbulent_Car_9629
- **Parent:** t1_mkzjezy
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkzxbhu/

> Whenever I see a hot girl I automatically skip the video; all AI videos nowadays look the same, creepy hot girls moving in a creepy slow-motion with creepy AI music. It’s becoming increasingly boring. I’m only after creative stuff that has real substance in it.

### t1_ml0sk6y (score=3, depth=0)
- **Author:** u/OuterWorldsAI
- **Parent:** t3_1jor1t4
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/ml0sk6y/

> I also got an impression (from the clips I've seen) that Gen-4 doesn't really feel like a whole generation above Gen-3, it feels more like they are trying to catch up with Kling and Luma and an honest thing would be to call it Gen-3.5. Sora on the one hand has amazing capabilities but is a) overpriced (for a 1080p version without a watermark) and b) is terrible at img2vid. I would say Luma Ray2 and Kling 1.6 have the best visual quality rn and Veo2 probably has the best prompt adherence. Don't know where exactly Gen-4 lands between those 3.

### t1_mku90by (score=2, depth=1)
- **Author:** u/Turbulent_Car_9629
- **Parent:** t1_mku6cl4
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mku90by/

> Hopefully they've still something to surprise us.

### t1_mkv0hc9 (score=1, depth=1)
- **Author:** u/possibilistic
- **Parent:** t1_mkuc5oh
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkv0hc9/

> Runway is trash. Try Kling. It's ten times better. 

### t1_mkzjezy (score=0, depth=0)
- **Author:** u/useapi_net
- **Parent:** t3_1jor1t4
- **Link:** https://www.reddit.com/r/runwayml/comments/1jor1t4/gen4_honest_opinion_disappointing_but_better_than/mkzjezy/

> I strongly disagree; I played a bit with Gen-4 today and it's very much in my books.  
> Here's a demo reel: two stitched 10-sec clips, 50% slowmo - 100% Gen-4 [https://useapi.net/blog/250402](https://useapi.net/blog/250402)  
> The whole thing took 5 shots total (had to throw away only 3 clips which is quite good imho)  
> Music is by Mureka AI.
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** Major Issues with Kling AI: Unusable Results Despite Premium Subscription
**Post URL:** https://www.reddit.com/r/KlingAI_Videos/comments/1gwvw5h/major_issues_with_kling_ai_unusable_results/
**JSON URL:** https://www.reddit.com/r/KlingAI_Videos/comments/1gwvw5h.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 20
- **extracted_unique_comments:** 19
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 0.95
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (1)

### t1_lydybbw (score=3, depth=0)
- **Author:** u/Science2013
- **Parent:** t3_1gwvw5h
- **Link:** https://www.reddit.com/r/KlingAI_Videos/comments/1gwvw5h/major_issues_with_kling_ai_unusable_results/lydybbw/

> Please only vote if you are using image to video as well
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** everything I learned after 10,000 AI video generations (the complete guide)
**Post URL:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/
**JSON URL:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 100
- **extracted_unique_comments:** 70
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 0.7
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (18)

### t1_na2f4ws (score=2, depth=0)
- **Author:** u/The_Poster_Children
- **Parent:** t3_1mvfcrr
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/na2f4ws/

> You know if you have multiple emails you can get the free trial on all of them. Through GCP and veo3 ive saved in total about $3,000 just experimenting with free accounts. Granted I also do code generation, but google is very generous with free tiers and promotion, use it while you can!

### t1_naldm8z (score=1, depth=2)
- **Author:** u/AutoModerator
- **Parent:** t1_naldm6j
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/naldm8z/

> Hi there! Your post was automatically removed because your account is less than 3 days old. We require users to have an account that is at least 3 days old before they can post to our subreddit.
> 
> Please take some time to participate in the community by commenting and engaging with other users. Once your account is older than 3 days, you can try submitting your post again.
> 
> If you have any questions or concerns, please feel free to message the moderators for assistance.
> 
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/PromptEngineering) if you have any questions or concerns.*

### t1_nz799zk (score=1, depth=1)
- **Author:** u/AutoModerator
- **Parent:** t1_nz799ra
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/nz799zk/

> Hi there! Your post was automatically removed because your account is less than 3 days old. We require users to have an account that is at least 3 days old before they can post to our subreddit.
> 
> Please take some time to participate in the community by commenting and engaging with other users. Once your account is older than 3 days, you can try submitting your post again.
> 
> If you have any questions or concerns, please feel free to message the moderators for assistance.
> 
> *I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/PromptEngineering) if you have any questions or concerns.*

### t1_na6x44r (score=3, depth=1)
- **Author:** u/Kenjirio
- **Parent:** t1_n9rg45s
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/na6x44r/

> Since you’re using ai to comment on this, here’s my own custom made assistant’s commentary and let’s compare to see if what you wrote vs what I got from my system is better:
> 
> Alright, this is actually pretty solid. Dude figured out something most creators never get.
> 
> **What’s working:**
> 
> The systematic mindset shift is everything. “Volume + selection beats perfection” - that’s pure Hormozi thinking applied to AI video. Most people are still trying to craft the perfect prompt like it’s poetry. This guy cracked the code: it’s manufacturing, not art.
> 
> The cost optimization angle is HUGE leverage that everyone’s sleeping on. Finding resellers at 60-70% off Google’s pricing? That’s the difference between broke hobbyist and actual business operator. $30/minute kills experimentation. $10/minute makes volume testing viable.
> 
> Platform-specific optimization shows he actually gets distribution. One video reformatted for everywhere = amateur hour. Native content for each platform = pro move.
> 
> **Where I’m calling BS:**
> 
> “Making money from AI video” - but HOW MUCH and HOW? This smells like $2k/month side hustle energy, not real business. What’s the actual revenue model here? Selling videos to who? Client work? Course sales?
> 
> Ten months and 10,000 generations sounds impressive until you realize that’s 33 videos per day. That’s not strategic - that’s spray and pray with better systems.
> 
> **The real insight he’s missing:**
> 
> He’s optimized the PRODUCTION but hasn’t cracked the BUSINESS MODEL. All this technical mastery is worthless if you can’t answer: “Who pays me, for what, and why?”
> 
> The …

### t1_nqhuc8t (score=3, depth=0)
- **Author:** u/Distinct-Mistake3480
- **Parent:** t3_1mvfcrr
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/nqhuc8t/

> This is solid stuff. The seed workflow and camera notes are exactly what most folks skip. My biggest breakthrough was realizing motion matters more than the perfect idea. If the camera jitters, the clip dies.
> I’ve been doing batches in higgsfield lately because I can chain small scenes with their multi-shot setup. Makes it easier to test different hooks without burning time. Sora enhancer keeps things steady too, so I don’t waste credits on shaky clips. Kinda lines up with your whole system over creativity idea.

### t1_n9vxekk (score=1, depth=0)
- **Author:** u/Safe-Owl-1236
- **Parent:** t3_1mvfcrr
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/n9vxekk/

> Those who are looking for free unlimited text to video generation  may prefer this PigenAi[PigenAi](http://pigenAi.art) though video quality is not that good but it's offering free unlimited generations

### t1_nleknpz (score=1, depth=1)
- **Author:** u/Empty_Chipmunk_1838
- **Parent:** t1_na2f4ws
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/nleknpz/

> are you talking about the 300$ free credits at GCP? is Veo3 included in it?

### t1_nlel0vz (score=1, depth=1)
- **Author:** u/Empty_Chipmunk_1838
- **Parent:** t1_na4h381
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/nlel0vz/

> Most of those models are close sourced, and building such workflows with open source models with decent quality isn't easy job, and when it comes to GPU, for video generation workflows you'd need GPU with 80GB VRAM

### t1_n9rg45s (score=14, depth=0)
- **Author:** u/[deleted]
- **Parent:** t3_1mvfcrr
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/n9rg45s/

> [removed]

### t1_n9r7ks0 (score=12, depth=0)
- **Author:** u/TrueDookiBrown
- **Parent:** t3_1mvfcrr
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/n9r7ks0/

> this person is personally responsible for a pond somewhere in the world drying up.

### t1_n9s2vgr (score=7, depth=0)
- **Author:** u/alexrada
- **Parent:** t3_1mvfcrr
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/n9s2vgr/

> cool insights, thanks. Saving this for later.

### t1_n9swub6 (score=6, depth=0)
- **Author:** u/imsid03
- **Parent:** t3_1mvfcrr
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/n9swub6/

> Worth saving the information, thanks

### t1_n9r801r (score=5, depth=0)
- **Author:** u/Area51-Escapee
- **Parent:** t3_1mvfcrr
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/n9r801r/

> What's a seed library? A seed is just for initializing a random number generator. I don't see how reusing the same seed for different videos would help.

### t1_n9rdl8r (score=4, depth=0)
- **Author:** u/Mysterious-Can3249
- **Parent:** t3_1mvfcrr
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/n9rdl8r/

> This is very helpful; thanks for sharing !! I’m just curious if you could share some financial numbers to get a sense of the results to be expected realistically compared to the effort that’s set.

### t1_n9vhpl5 (score=3, depth=0)
- **Author:** u/JCII100
- **Parent:** t3_1mvfcrr
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/n9vhpl5/

> Please post several examples

### t1_naldm6j (score=1, depth=1)
- **Author:** u/[deleted]
- **Parent:** t1_n9r801r
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/naldm6j/

> [removed]

### t1_nz799ra (score=1, depth=0)
- **Author:** u/[deleted]
- **Parent:** t3_1mvfcrr
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/nz799ra/

> [removed]

### t1_na4h381 (score=1, depth=0)
- **Author:** u/dontbelieveawordof1t
- **Parent:** t3_1mvfcrr
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mvfcrr/everything_i_learned_after_10000_ai_video/na4h381/

> Curious, why use credits vs buy a machine with a high end GPU if you are doing that much inference?
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** My complete AI video workflow that generates 20+ videos per week (systematic approach)
**Post URL:** https://www.reddit.com/r/PromptEngineering/comments/1mzan5d/my_complete_ai_video_workflow_that_generates_20/
**JSON URL:** https://www.reddit.com/r/PromptEngineering/comments/1mzan5d.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 11
- **extracted_unique_comments:** 9
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 0.8182
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (5)

### t1_ntbbdlp (score=1, depth=0)
- **Author:** u/Sad-Cauliflower-4605
- **Parent:** t3_1mzan5d
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mzan5d/my_complete_ai_video_workflow_that_generates_20/ntbbdlp/

> Super impressive workflow — love how structured your weekly system is. I’ve been testing Vizard alongside my generation stack, mainly for the repurposing side. It auto-pulls multiple strong clips from long videos, gives them viral scoring, and the editor lets me tweak subtitles like editing text. The scheduling + calendar also makes the Friday batch-finalization step smoother. Might be worth trying as an add-on layer if you ever want to streamline the post-gen pipeline.

### t1_najhe3y (score=7, depth=0)
- **Author:** u/wandsworth
- **Parent:** t3_1mzan5d
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mzan5d/my_complete_ai_video_workflow_that_generates_20/najhe3y/

> It seems like the same person is flooding all the AI/prompt subs with similar content under different usernames.
> 
> 
> https://www.reddit.com/r/PromptEngineering/comments/1mz1wh6/how_i_went_from_800_in_failed_ai_generations_to/?utm_source=share&utm_medium=mweb3x&utm_name=mweb3xcss&utm_term=1&utm_content=share_button
> 
> 
> https://www.reddit.com/r/PromptEngineering/comments/1mzauni/every_beginner_mistake_i_made_with_ai_video_and/?utm_source=share&utm_medium=mweb3x&utm_name=mweb3xcss&utm_term=1&utm_content=share_button

### t1_najaw6b (score=3, depth=0)
- **Author:** u/or45t
- **Parent:** t3_1mzan5d
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mzan5d/my_complete_ai_video_workflow_that_generates_20/najaw6b/

> Side question: are people still earning from AI videos? I was under the impression that platforms stopped paying for AI generated content. Or was it just youtube?

### t1_najwmm3 (score=3, depth=2)
- **Author:** u/wandsworth
- **Parent:** t1_najw2ds
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mzan5d/my_complete_ai_video_workflow_that_generates_20/najwmm3/

> Promoting veo3.gen app, it seems

### t1_najw2ds (score=1, depth=1)
- **Author:** u/reditsagi
- **Parent:** t1_najhe3y
- **Link:** https://www.reddit.com/r/PromptEngineering/comments/1mzan5d/my_complete_ai_video_workflow_that_generates_20/najw2ds/

> notice this too in other sub or topics.. What is their purpose?
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** I built a fully automated AI video factory. Here's the Make + AI workflow
**Post URL:** https://i.redd.it/qtvr5g4q0chf1.jpeg
**JSON URL:** https://www.reddit.com/r/automation/comments/1mivv0a.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 11
- **extracted_unique_comments:** 10
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 0.9091
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (1)

### t1_n78imdq (score=5, depth=0)
- **Author:** u/squirtinagain
- **Parent:** t3_1mivv0a
- **Link:** https://www.reddit.com/r/automation/comments/1mivv0a/i_built_a_fully_automated_ai_video_factory_heres/n78imdq/

> Stop. You're contributing nothing. We don't need more slop.
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** How are you automating 1,000+ product showcase videos from photos?
**Post URL:** https://www.reddit.com/r/automation/comments/1q9xvhw/how_are_you_automating_1000_product_showcase/
**JSON URL:** https://www.reddit.com/r/automation/comments/1q9xvhw.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 9
- **extracted_unique_comments:** 9
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 1.0
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (2)

### t1_nz2ub7t (score=1, depth=0)
- **Author:** u/RobbyInEver
- **Parent:** t3_1q9xvhw
- **Link:** https://www.reddit.com/r/automation/comments/1q9xvhw/how_are_you_automating_1000_product_showcase/nz2ub7t/

> Task scheduler running API's to various video generators that have API's (eg. Runway) then stitch sound, text and voice using ffmpeg based automators and finally using another api to upscale to 2k and 4k.
> 
> Titles are created from script using imagickmagick and PHP. Music is AI generated to match either length or mood (if mood then it's just a repeating loop).
> 
> Source videos are cropped or canvas expanded if necessary to fit on portrait (eg. TikTok), square (Instagram) and horizontal (YouTube) formats.
> 
> Ffmpeg also used to modify sounds levels at each point in time (eg. By 30%) whenever the AI voiceover speaks.
> 
> At the end ffmpeg also used to insert both metadata and thumbnails into each video, and at all stages write the status to an online myqsl DB, so that errors and flags can be sent via email if anything jams (mostly due to all backup gen platforms not working when one goes down).
> 
> For more complicated videos, pipeline is paused while an automated prompt (usually email) is sent with link to approve or reject (eg. Video generated before music, titling and voiceover insertion). If rejected the process for that stage is simply repeated.
> 
> Each video we produce in this pipeline takes anywhere from 2 to 6 hours to render (shorter if there's little movement or no need to upscale beyond 2k).

### t1_nyymfqy (score=1, depth=0)
- **Author:** u/stacktrace_wanderer
- **Parent:** t3_1q9xvhw
- **Link:** https://www.reddit.com/r/automation/comments/1q9xvhw/how_are_you_automating_1000_product_showcase/nyymfqy/

> We looked at something similar when marketing wanted volume without turning it into a manual edit factory. What helped was getting ruthless about templates and constraints, same camera moves, same clip order, same text rules, then letting automation fill the slots. The moment we allowed per product creativity, it broke down fast and needed human cleanup. In our case, batching and deterministic inputs mattered more than squeezing quality out of each clip. It did not look cinematic, but it was predictable and scaled without constant babysitting. I would focus less on the video model and more on locking the workflow so it cannot drift.
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** what I learned from burning $500 on ai video generators
**Post URL:** https://www.reddit.com/r/automation/comments/1pdkrwj/what_i_learned_from_burning_500_on_ai_video/
**JSON URL:** https://www.reddit.com/r/automation/comments/1pdkrwj.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 18
- **extracted_unique_comments:** 12
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 0.6667
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (2)

### t1_ns8f3j6 (score=1, depth=0)
- **Author:** u/lucaslamou
- **Parent:** t3_1pdkrwj
- **Link:** https://www.reddit.com/r/automation/comments/1pdkrwj/what_i_learned_from_burning_500_on_ai_video/ns8f3j6/

> Excellent breakdown! As someone working with batch video processing via APIs, I'd add:
> 
> 
> 
> \*\*For automation workflows:\*\*
> 
> \- Combine multiple tools: Use Runway Gen-4 for variety, Agent Opus for consistency
> 
> \- API integration is key: Most have REST APIs for programmatic batch processing
> 
> \- Consider cost per asset: Track actual $/video instead of monthly subscriptions
> 
> \- Implement quality gates: Automated review before final output saves hours
> 
> 
> 
> \*\*Hidden costs:\*\*
> 
> \- Version control for prompts (what generation that worked well?)
> 
> \- Cleanup workflow: Scripts to re-encode, match aspect ratios
> 
> \- Iteration cycles: Plan for 2-3 generations per final asset
> 
> 
> 
> \*\*For production use:\*\*
> 
> \- Combine with orchestration (Zapier/n8n) to trigger generation on schedule
> 
> \- Use version control on API keys and prompts
> 
> \- Test on free tier first to validate workflow before scaling
> 
> 
> 
> The $500 is valuable learning data. The real cost is operational efficiency once you automate the selection + iteration process.

### t1_ns79j06 (score=6, depth=0)
- **Author:** u/Framework_Friday
- **Parent:** t3_1pdkrwj
- **Link:** https://www.reddit.com/r/automation/comments/1pdkrwj/what_i_learned_from_burning_500_on_ai_video/ns79j06/

> This is a solid breakdown, appreciate you actually testing these and sharing what worked versus what burned budget. The pattern you're hitting is something we see constantly: tools are impressive in demos but fall apart in production workflows. The real cost isn't the $500 on generators, it's the hours spent stitching outputs together, fixing inconsistencies, and babysitting each generation until it's usable.
> 
> We've been building automation workflows that treat these AI video tools as components in a larger system rather than standalone solutions. The orchestration layer handles the repetitive parts like feed in assets, generate variations, route based on quality checks, archive what works, retry what doesn't. Turns out the boring workflow automation around the flashy AI tools is what actually saves time and money.
> 
> For agency work especially, the bottleneck isn't generation speed, it's the manual review and iteration cycles. Automating those handoffs between tools, client feedback loops, and asset management tends to have bigger ROI than finding the perfect generator.
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** What’s the current frontier in AI-generated photorealistic humans?
**Post URL:** https://www.reddit.com/r/artificial/comments/1mi9y9m/whats_the_current_frontier_in_aigenerated/
**JSON URL:** https://www.reddit.com/r/artificial/comments/1mi9y9m.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 79
- **extracted_unique_comments:** 56
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 0.7089
- **stop_reason:** completed
- **requests_total:** 1
- **requests_morechildren:** 0

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (8)

### t1_n72jpug (score=3, depth=0)
- **Author:** u/RobertD3277
- **Parent:** t3_1mi9y9m
- **Link:** https://www.reddit.com/r/artificial/comments/1mi9y9m/whats_the_current_frontier_in_aigenerated/n72jpug/

> Legally speaking from proposed legislation coming out of Europe, any AI generated human representations will have to have a very clear disclaimer at the beginning of a video. Because of the nature of the work and the problem with deep fakes, manipulations, and other severe problems that are being addressed, more than likely this will be an audio disclaim with that must be clear and the present.
> 
> Here are a few examples of deepfakes doing real world damage: 
> 
> https://incode.com/blog/25-million-deepfake-fraud-hong-kong/
> 
> https://incode.com/blog/top-5-cases-of-ai-deepfake-fraud-from-2024-exposed/#:~:text=An%20AI%2Dmanipulated%20audio%20clip,the%20World's%20Biggest%20Advertising%20Groups
> 
> There are other nefarious uses for it, some even suggesting that it could be used by governments and police to manufacture criminal activity as a means of getting rid of people they don't want that might be causing "political disturbances" or "uncomfortable situations". This technology can be very dangerous without very aggressive regulations, the problem is, we already know the government's always consider themselves above the law along with 90% of most politicians and elitists.
> 
> European Union legislation addressing AI issues:
> 
> https://www.bioid.com/2024/06/03/eu-ai-act-deepfake-regulations/#:~:text=Developers%20and%20users%20of%20deepfake,classification%20and%20watermarking%20of%20deepfakes.
> 
> Whether or not this framework actually does anything beneficial for the people that have the power and the money to abuse it is yet to be seen. There's also the question of the media faking and manipu…

### t1_n747423 (score=103, depth=0)
- **Author:** u/[deleted]
- **Parent:** t3_1mi9y9m
- **Link:** https://www.reddit.com/r/artificial/comments/1mi9y9m/whats_the_current_frontier_in_aigenerated/n747423/

> [removed]

### t1_n720iwd (score=7, depth=0)
- **Author:** u/[deleted]
- **Parent:** t3_1mi9y9m
- **Link:** https://www.reddit.com/r/artificial/comments/1mi9y9m/whats_the_current_frontier_in_aigenerated/n720iwd/

> I’m an AI Architect and my team has been testing looking to create life-like models for our products.  I have to say that none of them are ready for primetime…yet. You prompt “walking toward you” and they walk directly away. “Arm up” will result in arms down. Frustrating.

### t1_n72uq5i (score=1, depth=0)
- **Author:** u/Life_Yesterday_5529
- **Parent:** t3_1mi9y9m
- **Link:** https://www.reddit.com/r/artificial/comments/1mi9y9m/whats_the_current_frontier_in_aigenerated/n72uq5i/

> Just take a quick look in subreddits like comfyui or stablediffusion. Or do you mean avatars? Also advanced - closed and open source.

### t1_n724gub (score=7, depth=0)
- **Author:** u/Gentlegee01
- **Parent:** t3_1mi9y9m
- **Link:** https://www.reddit.com/r/artificial/comments/1mi9y9m/whats_the_current_frontier_in_aigenerated/n724gub/

> The lack of technical discussion around these tools is probably because they're still pretty new. I'm curious to see how they evolve in terms of ethics and usage guidelines

### t1_n72a2cn (score=4, depth=0)
- **Author:** u/[deleted]
- **Parent:** t3_1mi9y9m
- **Link:** https://www.reddit.com/r/artificial/comments/1mi9y9m/whats_the_current_frontier_in_aigenerated/n72a2cn/

> What I’m curious about is the ethical + legal front. Some of these avatars are getting so good, it's hard to tell if you're watching a real actor. We need better frameworks before this becomes mainstream in media.

### t1_n73z2fl (score=4, depth=1)
- **Author:** u/Richard7666
- **Parent:** t1_n720iwd
- **Link:** https://www.reddit.com/r/artificial/comments/1mi9y9m/whats_the_current_frontier_in_aigenerated/n73z2fl/

> Former animator here.
> 
> I feel trying to control the overall direction via text rather than via bones with the occasional keyframe would be extremely slow and unintuitive, even if it did interpret intent more accurately.
> A rigged character that the "AI" then renders over top of would be the ideal control mechanism.
> 
> Otherwise it'd be like trying to play an FPS by typing where you want to go instead of just using the mouse.

### t1_n78i0j3 (score=3, depth=1)
- **Author:** u/Funny-Permission2973
- **Parent:** t1_n747423
- **Link:** https://www.reddit.com/r/artificial/comments/1mi9y9m/whats_the_current_frontier_in_aigenerated/n78i0j3/

> How long does it take to make a full clip with Modelsify?
# Reddit Comment Extraction (Best-effort, No OAuth)

**Post Title:** What's your take on AI-generated video? Useful? Useless? Somewhere in between?
**Post URL:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/
**JSON URL:** https://www.reddit.com/r/premiere/comments/1m7etdp.json?raw_json=1&sort=top&limit=300&depth=10

## Coverage metrics

- **expected_num_comments:** 327
- **extracted_unique_comments:** 317
- **remaining_pending_child_ids:** 0
- **missing_children_ids:** 0
- **coverage_estimate:** 0.9694
- **stop_reason:** completed
- **requests_total:** 2
- **requests_morechildren:** 1

## Analysis instructions

- Filter baseline: `score >= 3` (unless signal is strong)
- Keep parent context when a reply is selected
- Run free solution check on top visible suggestions

## Selected comments (54)

### t1_n4rjgs8 (score=8, depth=1)
- **Author:** u/MrBobDobolina
- **Parent:** t1_n4qy7e4
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4rjgs8/

> I love that Premiere does transcript generation for free, but the editing process is clunky. For many of my videos I'm paying 50 cents/minute to transcribe them simply because of how easy to use the software is. 
> 
> 
> 
> (I use SpeedScriber to do the transcription and make corrections to the captions, then export as an SRT, pull that into Premiere to double check the timings and do the final export with burned in captions.)

### t1_n4sqefc (score=3, depth=1)
- **Author:** u/Jason_Levine
- **Parent:** t1_n4rhwz3
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4sqefc/

> Hey batch. Another rational endorsement for Stock footage as an alternative, not necessarily because of quality, but because the TIME involved isn't much different, and in many cases, the generative side  is significantly longer because prompting to get what you want can be...a process to say the least. 
> 
> Totally appreciate the 'sprinkle the silliness' sentiment tho, and others have echoed the same
> 
> Re: AE... been seeing a lot lately around leveraging generated assets (largely in the form of organic backgrounds, color animated background meant as backing plates or overlays) as a part of a traditional AE vfx workflow (used as new, visually hard to create manually, element).

### t1_n59vyve (score=1, depth=2)
- **Author:** u/EvilBobster101_
- **Parent:** t1_n4rjgs8
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n59vyve/

> that “free” transcript generation actually costs $60 a month

### t1_n4rkonn (score=5, depth=0)
- **Author:** u/cameranerd
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4rkonn/

> AI generated video is not a substitute for the real thing. I don't plan to use it in my work and I hope Adobe doesn't spend time or money developing new image generating tools. 
> 
> I love the [Adobe Podcast Enhance Speech](https://podcast.adobe.com/en/enhance) tool though. I know you're working to further integrate it into Premiere. That's the type of AI that is useful to my workflow, not AI generated images.

### t1_n500269 (score=1, depth=1)
- **Author:** u/Key-Boat-7519
- **Parent:** t1_n4v1rkc
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n500269/

> AI video is best treated like any other plugin: a timesaver, not the final storyteller. For client reels I drop a low-res copy into Runway to strip boom poles, export the clean plate, then pass only that slice through Topaz Video AI to recover detail before comping it back in Premiere. Shot tracking stays solid because I keep the metadata from the original clip. Workflows move faster if every AI layer gets its own track and a \_GEN suffix so the team can swap it out when standards change. I’ve tested Topaz Video AI and Runway, but AdComposer AI mostly rides shotgun when I need tight social copy that lines up with the finished cuts. Used right, it’s just another power tool, not a shortcut.

### t1_n50jy5q (score=1, depth=2)
- **Author:** u/wrosecrans
- **Parent:** t1_n4rjgs8
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n50jy5q/

> > I love that Premiere does transcript generation for free, but the editing process is clunky. 
> 
> Yeah.  I recently played with, despite being one of the grumpy old farts who automatically defaults to avoiding most of the AI stuff.  I wanted to see if the actor had said a line a certain way in any of the takes.  Premiere had transcribed the files, so theoretically easy.  But I had to click on each file, one by one, to search the transcripts separately.
> 
> If I was using a computer from the 1980's and I had a directory full of text files that I wanted to search for a phrase, I could do that in two seconds even if there were a zillion files.  The UX for the AI stuff seems to be rushed out and clunky, and they skip over kind of basic already-solved stuff that I would expect to be easy on a 40 year old computer, to implement the really fancy stuff.  The AI model doing the speech recognition was generally pretty good.  The transcript itself on any given file was fine to good.  (It would be better if I could easily point it at the text of the screenplay as a word source for the recognition dictionary!  Narrowed model speech recognition worked perfectly fine in the 1990's, even with unique sci fi jargon.)  But the focus 100% on the "sexy" AI guts part, and the UX for stuff like "search and filter text" gets a back seat because that doesn't generate hype.  It just gets bolted on from an implementation-first orientation, and not thought about from use-case-first orientation.

### t1_n4qyfui (score=9, depth=0)
- **Author:** u/realmattmormann
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4qyfui/

> I think the best use of AI would be to help cover for mistakes or enhance what was already shot. I’m thinking of how I really like the Enhance Speech AI tool for audio. Things like that I think I would find most helpful. I don’t think I have much of a need for being able to just generate whatever I want, but I do think there’s potential use in extending clips, removing logos, sharpening an out of focus shot, or helping with resolution changes off the top of my head. The company I work for is trying to integrate our print writers into doing more video work and sometimes their shots need some love

### t1_n4r67pf (score=6, depth=0)
- **Author:** u/lion-island
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4r67pf/

> There's a use case that's not really been spoken about and I think would be a far more useful addition, AI sharpening. 
> 
> Say I shot something and it lost focus for a split second, or even was purely defocused, it would be incredible to have AI reproduce the image to save the shot. But the 1080p limitation currently imposed means I can't ever use any current AI models (I need 4k in my workflow to provide wide and vertical crops without any loss, and I'm sure a lot of others are in the same boat there). 
> 
> Or even AI upscaling would be great to bring in. Topaz surely aren't the only ones able to do this?

### t1_n4qugok (score=69, depth=0)
- **Author:** u/xScareCrrowx
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4qugok/

> It’s (mostly) useless. And an even more useless thing to focus on considering how bad of a state premiere is in. Needs to be remade for modern standards from the ground up. I couldn’t give a damn less about poorly ai generated video that’s gonna be expensive anyway.

### t1_n4xreir (score=4, depth=1)
- **Author:** u/Capital-Programmer88
- **Parent:** t1_n4qy7e4
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4xreir/

> As an actor, I wanna say thank you - honestly couldn't have said it better.
> 
> I will add my two cents though, generative AI has no place in the creative process and dehumanises the exact thing that sets us apart from any other living thing - the ability to create. 
> 
> If you give everyone the ability to make blockbuster-level cinematics through AI, we will eventually lose Indie filmmakers.
> 
> It's already happening in the music industry with Deezer reporting 20,000 ai AI-generated songs DAILY being uploaded to their platform - I'll type that again - twenty thousand a day. This makes up 18% of their entire library. 
> 
> It's already happening and it won't stop any time soon, unless companies like Adobe push to protect the people and industries they rely on to keep them in business.

### t1_n4rghrc (score=1, depth=0)
- **Author:** u/cuddlesdacobra
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4rghrc/

> AI gen video has been mostly useless other than a sort of neat party trick. Anytime I’ve tried to use it seriously in a project project it becomes a waste of time and I end making or shooting the asset or finding a creative work around. 
> 
> Now I would love to see some LLM integration in the Text panel working with transcripts.  For example being able to ask it to put together a 5 minute sound bite select reel from a raw hour long interview. Or take selects I’ve pulled and order them into a rough  story.

### t1_n4sotjx (score=3, depth=2)
- **Author:** u/mikechambers
- **Parent:** t1_n4s7aaj
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4sotjx/

> Yes. So much of the conversation around AI has been around Generative AI (image / video). I think it has its place, but where the real value is, i.e. where it really help scale up the creator, is if you start thinking about AI / agents as a team that can help you with all of the stuff around creating (i.e. planning, brainstorming, scripting tools, etc....).
> 
> Creation is just one part of the overall set of tasks creators / editors have to do. The big opportunity is to let AI help with all of the other parts of that process outside of the actual creation.

### t1_n4qtve4 (score=47, depth=0)
- **Author:** u/Depreston
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4qtve4/

> Dog shit. That's my opinion on gen-ai video. Anyone who uses it in their films are a stain on society

### t1_n4qy7e4 (score=42, depth=0)
- **Author:** u/ArthurWhorgon
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4qy7e4/

> The only real thing I've seen AI be genuinely useful for is transcripting, and is probably the one thing I'd like out of premiere the most. Premiere's current automatic transcript generation is seriously lacking. It capitalizes random words and doesn't understand when people are actually done talking. I've seen other programs use some form of AI to enhance transcription and it saves me a massive headache, I'd love to see it be implemented in some way.
> 
> However, when it comes to AI-video generation, I can't say I see any use case for it, in really any way. I had a shot that unfortunately cut a little before we wanted, so we tried using the generative extend tool to get a few more seconds out of it, and it was absolutely unusable. It muddied the footage and was immediately noticable as AI generated. I haven't touched the feature since.
> 
> My issue with AI (beyond it's environmental and ethical/moral implications) is mainly on it being shoved into programs with little real use case that isn't either far too expensive and just as time consuming as doing it yourself, or immediately instills a new form of uncanny valley within me and everyone who sees it. It can be wildly useful and I'll admit I actually think it's kind of cool, but until we can find a way to implement it as a tool without using a massive amount of energy, as well as find more use cases beyond "I made a video of Barrack Obama getting arrested isn't that funny," I don't really see any reason to go near AI-video generation.
> 
> It feels like those people in the 90s with giant VR headsets, except they decided to immedia…

### t1_n4rtf6d (score=3, depth=0)
- **Author:** u/EvilDuck80
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4rtf6d/

> Since most models were unethically trained, I try to avoid them like the plague. I did try some just for fun but never on actual projects. It's very tempting to use them for specific things (style transfers, assets generation, etc ) but most of the time I have a very specific mental image of what I want that no matter how much I try different prompts, I feel that I am wasting my time, like, in the time it takes the AI to generate things I could have just created the assets I need from scratch. 
> 
> Since Adobe's approach for the training was one of the most ethical ones (I recently learned about Moonvalley's Marey) and it comes with my subscription, I started to explore it more.
> 
> I tried it on simple motion graphics project. Very soon I realized that I was not going to be able to just use the generated videos as they were (no much control over camera movement, composition, etc) so I decided to just use Photoshop to create the frame references with a green background for keying and composite the elements in After Effects later. It basically became a game of creating references and trying prompts until I had an asset that I could use, and I still had to mask, freeze frames or tweak a lot of things in After Effects.
> 
> I like to have control over every element on a project (as most directors or art directors would) so using AI generated videos for individual assets instead of trying to make it generate the whole thing was a better approach for the kind of projects I work on. I still couldn't generate everything I needed so I had to combine generated videos with traditional layers …

### t1_n4qv5o4 (score=29, depth=0)
- **Author:** u/No_Tamanegi
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4qv5o4/

> Most of the video content I work with is of a high enough technical specificity that I doubt that AI will ever be able to be a benefit to me.

### t1_n4r07wp (score=26, depth=0)
- **Author:** u/zazarappo
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4r07wp/

> Garbage, as are the people who use it.

### t1_n4rc48c (score=1, depth=1)
- **Author:** u/Jason_Levine
- **Parent:** t1_n4r3r04
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4rc48c/

> Hey Toaster. Thanks for honest assessment (and yet another that I believe is shared among many).
> 
> I really liked this line in particular: *"As it turns out, this is fun for me, and I don't like the idea of the machine not only having my fun, but turning in worse work."* I agree that there's a trend (in the industry) that 'the process' is always and forever, a burden...and that's just not true. It \*can\* be true, sure... but it's not an absolute, especially when you're learning (but even when you're seasoned). One person's mundane task is another's Splash Mountain (ie, something fun; don't know why I went there. I guess I used to like Splash Mountain. lol) 
> 
> What do you think about using it for things like upscaling footage tho? Or (stepping outside of video) doing something like voice cleanup or stem separation? Still generative, but sourced from \*your\* content?

### t1_n4qwlhu (score=21, depth=2)
- **Author:** u/Depreston
- **Parent:** t1_n4qw02p
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4qwlhu/

> Haven't had to use it because im a creative editor and can use another shot or use an insert shot with music

### t1_n4r9wq6 (score=18, depth=2)
- **Author:** u/TryingMyWiFi
- **Parent:** t1_n4qxahq
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4r9wq6/

> I guess he was talking about genAI in general, and how it's not supposed to be a priority for adobe to focus on, given the overall bad state of their software .

### t1_n4ra1ny (score=18, depth=2)
- **Author:** u/No_Tamanegi
- **Parent:** t1_n4qxkh3
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4ra1ny/

> Upscaling/denoising would be great. Most of the content I work with is based around teaching electronics. So until AI can replicate "Solder green a jumper wire to Pin 7 of the Xiao RP2040 shown from a 3/4 view at a distance of 3"" It's going to be easier to just film it.
> 
> Consistency is really important too - the tools, hardware, and elements should all be consistent throughout the video. If they're not, then I'm failing my job as an editor.

### t1_n4qzhvp (score=17, depth=0)
- **Author:** u/s09gtn
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4qzhvp/

> I use it to storyboard concepts. I use it for transcriptions. I’m open to using it for tagging metadata. Nothing more.
> 
> I don’t think general public is even close to accepting it as either a full-on replacement for creative art or being sold a product. It feels fake and cheap and contributing to un-reality.

### t1_n4z9pxy (score=1, depth=6)
- **Author:** u/renandstimpydoc
- **Parent:** t1_n4xjiy8
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4z9pxy/

> ❤️
> Feel free to DM me if you have any questions. 

### t1_n5xtkou (score=1, depth=0)
- **Author:** u/Altruistic-Pace-9437
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n5xtkou/

> Ia-generated video is like non-alcoholic beer or a rubber woman. If everyone was using it for doing something good... But there are tons of rubbish-content in the internet now. The only way I see it useful is giving the opportunity to change video angles and only if it was free.

### t1_n4rorf4 (score=9, depth=0)
- **Author:** u/[deleted]
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4rorf4/

> [deleted]

### t1_n4r5x52 (score=3, depth=0)
- **Author:** u/amindada1971
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4r5x52/

> I use it for pre-vis /  storyboards. It’s really helpful as our studio time is limited. Can be a frustrating experience sometimes as a great result is often destroyed with removal / change of a single word! 
> 
> I’m sure it’s great for lone wolf outfits but for teams not so much because once feedback comes in it’s pretty much uncontrollable.

### t1_n4rj1d7 (score=8, depth=0)
- **Author:** u/polarsis
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4rj1d7/

> I respect myself and the crafts of videography and editing, so I wouldn't be caught dead using it - and any 'professional' that uses AI video should be ashamed of themselves.

### t1_n4rpba1 (score=7, depth=1)
- **Author:** u/SlashMatrix
- **Parent:** t1_n4qy7e4
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4rpba1/

> Thank you. Because you wrote this, I don't have to. I couldn't have said any of this better myself.

### t1_n4r9zb8 (score=6, depth=2)
- **Author:** u/s09gtn
- **Parent:** t1_n4r7tx2
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4r9zb8/

> It also turns people off very much to see this AI generated content of president being arrested in the Oval Office or what their fictional self would look like behind bars, along with those in power abusing this technology. Until it cleaned up and even semi-regulated, at best it will be viewed as something either 100% scroll-past-entertainment (ie Will Smith eating spaghetti) or 100% dangerous (ie the above example).

### t1_n4ricro (score=5, depth=0)
- **Author:** u/MrBobDobolina
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4ricro/

> As a video editor the most useful thing I would want is the ability to stabilize a shaky clip (especially at the start or end of a clip) and maybe extend a clip for another second or two. I haven't used any of the AI that can do this yet, but that is what I see myself doing. The stock footage I'm looking for is often so specific sometimes need to make it myself. 
> 
> When I deal with churches, non-profits, or universities, these organizations must be trustworthy and my fear in using (anything) AI with their products is that the use of AI as a tool might erode the trust that they have built for their brand. If any of the places I edit for used AI video there would likely be some backlash.

### t1_n4rkapl (score=5, depth=2)
- **Author:** u/MrBobDobolina
- **Parent:** t1_n4r5ld5
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4rkapl/

> Yeah, if there was a way to eliminate an accidental camera bump when you hit the tripod or the floor is a bit soft and someone walks past and everything shakes a little... I'd use that. (Warp Stabilizer would require the clip to be zoomed in to fix this, maybe image generation wouldn't?) 
> 
> Along those lines, warp stabilizer sometimes doesn't do well when multi-axis are moving, anything AI could do to improve that?

### t1_n4torm6 (score=5, depth=3)
- **Author:** u/JohnGacyIsInnocent
- **Parent:** t1_n4r9wq6
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4torm6/

> I feel a little crazy at the moment for not seeing the major issues with Premiere. I use it all day, every day alongside Ae and my issues are very few and far between.

### t1_n4qzcm9 (score=4, depth=1)
- **Author:** u/Jason_Levine
- **Parent:** t1_n4qy7e4
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4qzcm9/

> Hey Arthur. This was really good feedback. The part that resonated the most (and a point I've been sharing w/other colleagues) is around the 'time' factor, ie, *"...just as time consuming as doing it yourself."*   
>   
> While I can see some use cases (at present), the misconception that it's somehow 'immediate' (and doesn't require subsequent generations and re-prompting and editing prompts over and over) is really a huge miscalculation. Again, not supporting one over the other, but that's a reality that sometimes get missed in initial dismissals (ie, that it's automatic and saves so much time).   
>   
> Also...the VR of the 90s comment...haha...I remember that period so well (I was involved in some productions of the time that leveraged the binaural soundtracks that were meant to accompany the video content of that craze). What a bust that was. lol. Thanks again.

### t1_n4rhb3m (score=4, depth=2)
- **Author:** u/ToasterCommander_
- **Parent:** t1_n4rc48c
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4rhb3m/

> Very genuinely man, when I needed audio cleaned up, I called my friend who knows audio. We hung out, cleaned up my mess, and went to the diner afterward. That human connection is part of why I do what I do, and I needed that reminder. Even if the machine could do his job, I'd prefer to work with someone who actually cares about doing quality work and doing right by me. 
> 
> I recognize not everyone has friends with those skills, but my deficiency led me to a good day with a friend and higher quality audio than a simple machine pass probably would have allowed with none of the hassle that would have come with it. 
> 
> Now, if I didn't have that friend? I'd probably still prefer to do that myself. Honestly, I'd prefer easily accessed tutorials well before I'd want the machine just doing shit for me. When the machine does some things, I, as an amateur, can't tell what it's doing. So if it makes mistakes, I won't know to catch them. And that, straight up, makes me worse as an editor.

### t1_n4rhwz3 (score=4, depth=0)
- **Author:** u/batchrendre
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4rhwz3/

> I think it’s cool but also I think the world is not currently capable of handling this technology responsibly. So 🤷
> 
> In my day to day, I think I’ve found if I am under deadline pressure, I’ll utilize stock library assets simply bc it’s currently faster to download video than generate video.
> 
> If I want to experiment and have fun on non-client work, I’ll play with Firefly or other tools, but very rarely. I’m usually working haha (thankfully!)
> 
> I think of generated video as a cool way to sprinkle some weird silliness into my personal videos, which is fun!
> 
> In general, I don’t love that it’s given my clients/the world this idea that my skill set can be replaced lol. Not saying I have all the skillz, but often, especially around motion design, I’ve found it faster in the long run to just fire up After Effects/Premiere and jump in than rely on generated assets completely.
> 
> Edit/TLDR:
> Feels like a cool Plugin I rarely remember to use that I downloaded illegally years ago before I started paying for plugins 😝

### t1_n4skbmp (score=4, depth=0)
- **Author:** u/Daguerratype42
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4skbmp/

> Mostly useless for now. The quality just isn’t there. There are two many obvious signs it’s AI generated, and I’m not talking extra fingers. The texture and lighting is always just… off, even on the latest and best models. If it gets better the utility could go up. 
> 
> Where I see AI being incredibly valuable as an edit is actually more around transcripts and search. Being able to quickly search large interview, for example. I really hope there features grow, and maybe even get editing action based on it. “Create a sting out of every clip where they talk about [insert topic]” for example. A prompt based assistant editor.

### t1_n4qw02p (score=3, depth=1)
- **Author:** u/Jason_Levine
- **Parent:** t1_n4qtve4
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4qw02p/

> Hey depreston. Appreciate the reply. What do you think about things like extending a frame or outpainting a scene? Sourced from video (you shot) but extended/expanded via LLM?

### t1_n4qxytn (score=3, depth=3)
- **Author:** u/Jason_Levine
- **Parent:** t1_n4qwlhu
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4qxytn/

> Yep, that's fair. That's generally where I fall as well.

### t1_n4r5ld5 (score=3, depth=1)
- **Author:** u/Jason_Levine
- **Parent:** t1_n4qyfui
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4r5ld5/

> Hey Matt. '*Their shots need some love'* is definitely a use case I lean towards as well. Really appreciat the comment.

### t1_n4rueb0 (score=3, depth=3)
- **Author:** u/realmattmormann
- **Parent:** t1_n4rkapl
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4rueb0/

> Warp Stabilizer is great when it works… I chuckle sometimes when it looks like the entire boat is rocking despite us being on land

### t1_n4toxyj (score=3, depth=2)
- **Author:** u/[deleted]
- **Parent:** t1_n4t7hdu
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4toxyj/

> [deleted]

### t1_n4tvv9j (score=3, depth=2)
- **Author:** u/No_Tamanegi
- **Parent:** t1_n4tveog
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4tvv9j/

> Resolution isn't the problem. Technical accuracy is. Read my followup comment if you're actually interested in my needs and don't just want to be condescending.

### t1_n4u04fg (score=3, depth=4)
- **Author:** u/Depreston
- **Parent:** t1_n4tvw2f
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4u04fg/

> My point is no working editor today needs generative extend because we know how to edit and cover mistakes. If you need generative extend then youre not that creative.

### t1_n4r3r04 (score=2, depth=0)
- **Author:** u/ToasterCommander_
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4r3r04/

> I think AI-generated everything is pretty much trash. To use a phrase my sister came up with, "I'm an A+ student and this thing can only give me C- work." Its uses are completely unknown to me, since anything I can ask it to do I can do better, and I'm an absolute amateur. It might take me more time, sure, but I'll not only have a better picture/cut/transition, but I'll have learned how to do it too. As it turns out, this is fun for me, and I don't like the idea of the machine not only having my fun, but turning in worse work. 
> 
> Straight up, I think if you use AI-generation, you're just cheap and lazy. That's all it says to me. And this is a very expensive program, so why the hell would I pay all this money every month just for people to look at my work and say "this looks cheap and lazy?"

### t1_n4qxahq (score=1, depth=1)
- **Author:** u/Jason_Levine
- **Parent:** t1_n4qugok
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4qxahq/

> Hey XScare. I wasn't specifically talking about Firefly, just generated video overall, but I appreciate the 'mostly' comment:) That said, the team has been watching the commentary here and is very focused on Premiere performance improvements. It takes time, but we're making progress.

### t1_n4s7aaj (score=1, depth=1)
- **Author:** u/sputnikmonolith
- **Parent:** t1_n4rghrc
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4s7aaj/

> Yes. 
> 
> This is what I was commenting on. Inventive uses for LLMs and machine learning to support and improve the tools, rather than useless generative shit.

### t1_n4t7hdu (score=1, depth=1)
- **Author:** u/Jason_Levine
- **Parent:** t1_n4rorf4
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4t7hdu/

> Hey AstroBjorn. It is the spirit in which you wrote your reply that makes me appreciate the community here. The digs at Adobe aside (I am an employee after all), I sincerely appreciate that you took the time and shared these thoughts in great detail; it's clearly very genuine. While I don't agree with it all, there are some undeniable realities you mention above that come along w/the territory in this new landscape, and they're not all great.

### t1_n4v1rkc (score=1, depth=0)
- **Author:** u/feelinn
- **Parent:** t3_1m7etdp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4v1rkc/

> I use it daily to expand backgrounds and foregrounds for social media content. Also adding stuff in the frame, then rotoscoping the foreground. Full generative stuff is currently not valid for publication (mostly) but not using the best tools for the job just because its AI doesnt make any sense. I think a lot of people are against AI, but there's a difference between being against AI and adamantly not using it because you dont believe in it.

### t1_n4xjiy8 (score=1, depth=5)
- **Author:** u/Jason_Levine
- **Parent:** t1_n4wvwjr
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4xjiy8/

> I can only imagine. But yes indeed, will be watching tomorrow night! Cannot wait. Soooo many memories from the early days. My interest has been genuinely piqued.

### t1_n4wvwjr (score=1, depth=4)
- **Author:** u/renandstimpydoc
- **Parent:** t1_n4u99og
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4wvwjr/

> Haha. Yeah. Was a rough year to release a film. Thanks for taking a look❣️

### t1_n4r7tx2 (score=0, depth=1)
- **Author:** u/Jason_Levine
- **Parent:** t1_n4qzhvp
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4r7tx2/

> Hey s09gtn. I'm totally with you on the general public comment; it's still early days, of course, but the un-reality/cheapness (<- nod to Zappa there;)) can't be ignored, in some instances. 
> 
> Another vote for the storyboard concept tho. That's very cool. Thanks again.

### t1_n4tvw2f (score=-1, depth=3)
- **Author:** u/Pure-Produce-2428
- **Parent:** t1_n4qwlhu
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4tvw2f/

> Because you’re a creative editor? Stain on society? Unless you’re at Rock Paper Scissors or cut tent pole films give me a break.

### t1_n4qxkh3 (score=-2, depth=1)
- **Author:** u/Jason_Levine
- **Parent:** t1_n4qv5o4
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4qxkh3/

> Hey No\_T. Very curious about the content you're working with and where that breaking point is. Even with upscaling or things of that nature?

### t1_n4tveog (score=-5, depth=1)
- **Author:** u/Pure-Produce-2428
- **Parent:** t1_n4qv5o4
- **Link:** https://www.reddit.com/r/premiere/comments/1m7etdp/whats_your_take_on_aigenerated_video_useful/n4tveog/

> What are you making 8K imax films for aliens with eyes that have 16k resolution? 
> 
> I’ve already put AI video in nationwide commercials. No one has a clue but those creatives will call me back because I made magic. But you won’t even investigate. Have you seen what Astra can do? And that’s freaking gen 1! Starlight takes old footage and makes it look amazing. I don’t mean like that weird Beatles film, I mean like straight up fresh. I’ve spent years in film color correction sessions, I have some semblance of knowledge. You definitely should at least keep your ear to the ground a bit.
