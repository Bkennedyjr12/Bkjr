// Minimal interactivity for the demo A.I. agent modal
document.addEventListener('DOMContentLoaded',function(){
  var launch=document.getElementById('launch-agent');
  var modal=document.getElementById('agent-modal');
  var close=document.getElementById('close-agent');
  var send=document.getElementById('agent-send');
  var input=document.getElementById('agent-input');
  var output=document.getElementById('agent-output');

  function openAgent(){ modal.setAttribute('aria-hidden','false'); input.focus(); }
  function closeAgent(){ modal.setAttribute('aria-hidden','true'); }

  if(launch) launch.addEventListener('click', openAgent);
  if(close) close.addEventListener('click', closeAgent);
  if(modal) modal.addEventListener('click', function(e){ if(e.target===modal) closeAgent(); });

  if(send){
    send.addEventListener('click', function(){
      var q = input.value.trim();
      if(!q){ output.textContent = 'Try typing a question for the agent (demo).'; return; }
      output.textContent = 'Thinking... (demo)

Response: This is a placeholder response. In production, this would call your private A.I. endpoint to summarize or draft content.';
    });
  }
});
