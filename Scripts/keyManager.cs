using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class keyManager : MonoBehaviour
{
    [SerializeField] GameObject player;
    public bool isPickedUp;
    public Vector2 velocity;
    public float smoothTime;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if(isPickedUp)
        {
            Vector3 offset = new Vector3(0,2f,0);
            transform.position = Vector2.SmoothDamp(transform.position, player.transform.position + offset, ref velocity, smoothTime);
        }
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if(other.gameObject.CompareTag("Player") && !isPickedUp)
        {
            isPickedUp = true;
        }
    }
}
